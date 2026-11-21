"""Exercise offline account behavior and authentication configuration."""
import subprocess
import tempfile
import unittest
from unittest.mock import patch
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JDK = Path('/usr/lib/jvm/java-17-openjdk-amd64/bin')


class OfflineAccountsTests(unittest.TestCase):
    def test_accounts_screen_always_lists_offline_option(self):
        source = (ROOT / 'launcher/java/orbis/launcher/LauncherScreen.java').read_text()
        self.assertIn('case ACCOUNTS -> accountList().size() + (microsoftLoginAvailable() ? 2 : 1);', source)
        self.assertIn('microsoftLoginAvailable() && selected == list.size()', source)
        self.assertIn('if (microsoftLoginAvailable()) {', source)
        self.assertIn('rows.add("Add offline account");', source)

    def test_release_workflow_allows_offline_only_build(self):
        workflow = (ROOT.parent / '.github/workflows/release.yml').read_text()
        self.assertIn('offline_only:', workflow)
        self.assertIn('if: ${{ !inputs.offline_only }}', workflow)
        self.assertIn("ORBIS_OFFLINE_ONLY: ${{ inputs.offline_only && '1' || '0' }}", workflow)

    def test_offline_only_build_skips_microsoft_client_resource(self):
        import importlib.util
        spec = importlib.util.spec_from_file_location('launcher_secrets', ROOT / 'tools/launcher_secrets.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        client = (ROOT / 'launcher/java/orbis/launcher/MicrosoftAuthClient.java').read_text()
        builder = (ROOT / 'tools/build_launcher.py').read_text()
        self.assertIn('OFFLINE_ONLY = "offline-only.bin"', client)
        self.assertIn('Microsoft sign-in is disabled in this offline-only test build.', client)
        self.assertIn('OFFLINE_ONLY_RESOURCE, b\'1\'', builder)
        with patch.dict('os.environ', {'ORBIS_OFFLINE_ONLY': '1', 'ORBIS_MSA_CLIENT_ID':
                                       '00000000-0000-0000-0000-000000000000'}):
            self.assertTrue(module.offline_only())
            self.assertIsNone(module.resource())

    def test_offline_store_has_no_microsoft_gate(self):
        source = (ROOT / 'launcher/java/orbis/launcher/AccountStore.java').read_text()
        self.assertNotIn('requireOwnedMinecraft()', source)
        self.assertNotIn('accounts.removeIf(account -> "offline".equals(account.kind()))', source)

    def test_premium_gate_and_offline_session(self):
        gson = ROOT / 'build/downloads/runner-jars/gson-2.8.9.jar'
        sources = ROOT / 'launcher/java/orbis/launcher'
        with tempfile.TemporaryDirectory() as output:
            subprocess.run([str(JDK / 'javac'), '--release', '17', '-Xlint:all', '-Werror',
                            '-cp', str(gson), '-d', output,
                            *[str(sources / name) for name in ('AccountStore.java', 'LauncherFiles.java',
                                                             'MicrosoftAuthClient.java', 'LaunchRequest.java')],
                            str(ROOT / 'tests/launcher/orbis/launcher/OfflineAccountsTest.java')], check=True)
            subprocess.run([str(JDK / 'java'), '-cp', output + ':' + str(gson),
                            'orbis.launcher.OfflineAccountsTest', str(Path(output) / 'accounts-test')], check=True)
