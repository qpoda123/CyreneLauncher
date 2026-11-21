"""Exercise the offline-only launcher and build configuration."""
import subprocess
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JDK = Path('/usr/lib/jvm/java-17-openjdk-amd64/bin')


class OfflineAccountsTests(unittest.TestCase):
    def test_home_screen_exposes_offline_login(self):
        source = (ROOT / 'launcher/java/orbis/launcher/LauncherScreen.java').read_text()
        self.assertIn('"Offline login"', source)
        self.assertIn('case 1 -> offlineLogin(source);', source)
        self.assertIn('private void offlineLogin(Input.Source source)', source)
        self.assertIn('case ACCOUNTS -> accountList().size() + 1;', source)
        self.assertIn('rows.add("Add offline account");', source)

    def test_build_completely_omits_microsoft_sign_in(self):
        workflow = (ROOT.parent / '.github/workflows/release.yml').read_text()
        builder = (ROOT / 'tools/build_launcher.py').read_text()
        self.assertNotIn('MicrosoftAuthClient', builder)
        self.assertNotIn('ORBIS_', workflow + builder)
        self.assertNotIn('offline_only', workflow)
        self.assertFalse((ROOT / 'launcher/java/orbis/launcher/MicrosoftAuthClient.java').exists())

    def test_offline_store_has_no_microsoft_gate(self):
        source = (ROOT / 'launcher/java/orbis/launcher/AccountStore.java').read_text()
        self.assertNotIn('requireOwnedMinecraft()', source)
        self.assertNotIn('accounts.removeIf(account -> "offline".equals(account.kind()))', source)

    def test_offline_profile_and_session(self):
        gson = ROOT / 'build/downloads/runner-jars/gson-2.8.9.jar'
        sources = ROOT / 'launcher/java/orbis/launcher'
        with tempfile.TemporaryDirectory() as output:
            subprocess.run([str(JDK / 'javac'), '--release', '17', '-Xlint:all', '-Werror',
                            '-cp', str(gson), '-d', output,
                            *[str(sources / name) for name in ('AccountStore.java', 'LauncherFiles.java',
                                                             'LaunchRequest.java')],
                            str(ROOT / 'tests/launcher/orbis/launcher/OfflineAccountsTest.java')], check=True)
            subprocess.run([str(JDK / 'java'), '-cp', output + ':' + str(gson),
                            'orbis.launcher.OfflineAccountsTest', str(Path(output) / 'accounts-test')], check=True)
