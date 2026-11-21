package orbis.launcher;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

/** Offline accounts are independent local profiles and do not require Microsoft sign-in. */
public final class OfflineAccountsTest {
    private OfflineAccountsTest() { }

    public static void main(String[] args) throws Exception {
        run(args.length == 0 ? Files.createTempDirectory("offline-accounts-") : Path.of(args[0]));
        System.out.println("Offline accounts passed");
    }

    static void run(Path root) throws Exception {
        Path home = root.resolve("home"), runner = root.resolve("runner");
        AccountStore store = new AccountStore(home, runner);
        check(!store.hasOwnedMinecraft(), "fresh installation has no Microsoft owner");
        AccountStore.Account offline = add(store, "LocalPlayer");
        check(offline.kind().equals("offline"), "creates an explicit offline profile");
        check(offline.uuid().equals("c6d762506d42328ebfce7a3312675f70"), "uses Minecraft's standard offline UUID");
        rejected(() -> add(store, "LocalPlayer"), "duplicate offline names are rejected");
        rejected(() -> add(store, "bad name"), "offline names must be valid Minecraft names");
        store.selectDefault(offline.id());
        AccountStore reopened = new AccountStore(home, runner);
        check(reopened.resolveAccount("").id().equals(offline.id()), "offline selection survives restart");
        // No Microsoft configuration exists: this must succeed without contacting authentication services.
        AccountStore.Session session = new MicrosoftAuthClient(reopened, home).refresh(offline.id());
        check(session.username().equals("LocalPlayer") && session.uuid().equals(offline.uuid()),
                "offline launch uses its own identity");
        check(session.accessToken().equals("0") && session.userType().equals("legacy")
                && session.xuid().isEmpty() && session.clientId().isEmpty(), "no premium tokens in offline sessions");
        check(LaunchRequest.decode(LaunchRequest.create("instance", offline.id()).encode()).accountId().equals(offline.id()),
                "offline identity survives the restart request");
        AccountStore.Account another = add(reopened, "Another");
        check(another.kind().equals("offline"), "additional offline profiles do not require Microsoft");
        reopened.remove(another.id());
        check(reopened.resolveAccount("").id().equals(offline.id()), "removing another profile preserves offline selection");

        Path failureHome = root.resolve("storage-failure");
        AccountStore failing = new AccountStore(failureHome, runner);
        AccountStore.Account failedOffline = add(failing, "LocalPlayer");
        failing.selectDefault(failedOffline.id());
        Path metadata = failureHome.resolve("accounts/accounts.json");
        byte[] previousMetadata = Files.readAllBytes(metadata);
        Files.delete(metadata);
        Files.createDirectory(metadata);
        rejected(() -> failing.putOffline("Another"), "offline profile storage failure is reported");
        Files.delete(metadata);
        Files.write(metadata, previousMetadata);
        AccountStore recovered = new AccountStore(failureHome, runner);
        check(recovered.resolveAccount("").id().equals(failedOffline.id()),
                "offline profile survives metadata recovery");
    }

    private static AccountStore.Account add(AccountStore store, String name) throws IOException {
        return store.putOffline(name);
    }

    @FunctionalInterface private interface Operation { void run() throws Exception; }
    private static void rejected(Operation action, String message) throws Exception {
        try { action.run(); } catch (IOException | IllegalArgumentException expected) { return; }
        throw new AssertionError(message);
    }
    private static void check(boolean condition, String message) {
        if (!condition) throw new AssertionError(message);
    }
}
