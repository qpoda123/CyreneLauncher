# Cyrene Launcher

Download and play supported game versions on your PS4 with local offline profiles. Cyrene Launcher manages separate game instances and browses mods and modpacks from Modrinth.

**[Download Cyrene Launcher](https://github.com/CyreneLauncher/CyreneLauncher/releases/latest)** · **[Report a problem](https://github.com/CyreneLauncher/CyreneLauncher/issues)**

This guide covers the current launcher. Older releases may have different menus or fewer features. Available versions and mods do not guarantee that every game or modpack will run correctly on PS4.

## What you need

- A PS4 already set up to install and run homebrew `.pkg` applications.
- A game version supported by the configured download source, or an already-installed version.
- Internet access for game, mod, and runtime downloads.
- Free console storage for the launcher, games, runtimes, mods, and worlds. Large modpacks need more space.
- A controller for launcher navigation. A keyboard and mouse are useful for Minecraft; controller gameplay depends on the game's controller mod and setup.

The package includes the launcher's Java runtime and graphics libraries. You do not need to compile anything or install Java manually. This build has no Microsoft sign-in; game downloads use the configured source.

## Install and launch

1. Open the [Releases page](https://github.com/CyreneLauncher/CyreneLauncher/releases/latest).
2. Download the **Cyrene Launcher `.pkg`** from the release's **Assets** section. GitHub's **Source code** archives are for developers, not installation.
3. Transfer the package to your PS4 using your usual homebrew package-installation method, then install it with your console's package installer.
4. Open **Cyrene Launcher** from the PS4 home screen.
5. Choose **Offline login** on the main screen and create a local player profile.

The launcher creates its settings and data folders on first launch. Offline login can download supported game versions and launch them without Microsoft sign-in.

## Launcher controls

The bottom of the screen shows controls for the device you last used.

| Action | Controller | Keyboard / mouse |
| --- | --- | --- |
| Move through a list | D-pad or stick | Arrow keys |
| Select or activate | Cross / ✕ | Enter or click |
| Go back or cancel | Circle / ○ | Escape |
| Switch Instances / Accounts | L1 / R1 | Page Up / Page Down or click the tab |
| Move between the instance list and its actions | Left / Right | Left / Right or Tab |
| Change a setting or loader | Left / Right | Left / Right |

Select a text field to edit it. With a controller, the PS4 system keyboard opens; with a physical keyboard, you can type directly. For physical keyboard entry, **Enter** accepts and **Escape** cancels the edit.

Some pages have extra controls. Follow the on-screen hints when searching, managing mods, or confirming an action.

## Offline login

Select **Offline login** on the main screen. If you have no profile yet, enter a player name (1–16 letters, numbers, or underscores). The profile is saved locally and selected for **Play**. To switch profiles or add another, open **Accounts** from the main screen and select a profile.

Offline profiles work with downloaded or installed game versions and single-player worlds. They do not authenticate with online-mode servers. This build does not include Microsoft sign-in; supported game versions can be downloaded from the configured source.

## Create your first Minecraft instance

An **instance** is a separate game setup with its own name, mods, settings, and worlds. Use separate instances to try different versions or modpacks without mixing their files.

This offline-only build can create instances from installed versions or download a supported version from the configured source.

1. Open **Instances** and choose **New instance** from the instance actions.
2. Choose the Minecraft-version option.
3. Select a loader with **Left / Right**:

   | Loader | Use it for |
   | --- | --- |
   | **Vanilla** | Minecraft without a mod loader |
   | **Fabric** | Fabric mods |
   | **Quilt** | Quilt, with Fabric mods offered by the launcher |
   | **Forge** | Forge mods, for Minecraft 1.18.2–1.21.11 |
   | **NeoForge** | NeoForge mods, for Minecraft 1.20.2–1.21.11 |

4. Select a Minecraft version and enter a name for the instance.
5. Wait for installation to finish. The launcher displays download progress.
6. Select the new instance and choose **Play**.

The current version browser offers releases from **1.14 through 26.3**, subject to loader availability. Forge and NeoForge use the ranges shown above; their year-numbered releases are not offered yet. Start with an unmodified instance before adding mods; older versions and demanding modpacks may need more troubleshooting.

The launcher chooses Java automatically. Games that need Java 21 or 25 download that runtime on first use, so their first installation or launch can take longer. Shared libraries and assets are reused across instances.

Forge and NeoForge installation also patches Minecraft. This takes longer than installing Fabric or Quilt. Keep the console running until the progress finishes. If installation is interrupted, retry; the launcher reuses verified downloads. Some installer tools need a newer Java runtime themselves. The launcher may restart to finish that installation, then finish creating your instance or installing your modpack and return to the menu.

Use mods made for your chosen loader: a Forge mod is not automatically a NeoForge mod. Packs retain the exact Forge/NeoForge build they request. Their games use the matching Java major version, and the launcher disables the loader's separate early-loading window so Minecraft owns the console display.

**Circle / Escape** cancels a download. A later installation attempt reuses and checks files that were already downloaded.

## Play and return to the launcher

Select an instance, move to its actions, and choose **Play**. Cyrene uses the selected offline profile and prepares the game. The application restarts as part of launching Minecraft, so a restart at this point is expected.

After you exit Minecraft, reopen Cyrene Launcher from the PS4 home screen to select another instance or change settings.

Launcher controller navigation and Minecraft controller gameplay are separate. For controller gameplay, install a compatible controller mod for your Minecraft version and configure it in-game. A keyboard and mouse can also be used.

## Install mods

1. Select the instance you want to change.
2. Open **Mods**, then the mod browser.
3. Search Modrinth and open a project to read its description and available versions.
4. Choose **Install** and review the required dependencies and any warnings.
5. Confirm installation, then launch the instance with **Play**.

The browser filters mods for the selected instance's game version and loader. Quilt instances are offered Fabric mods. Vanilla instances do not have a mod browser. Matching the version and loader does not guarantee PS4 compatibility, especially for mods that require additional native libraries. Java agents and mods that require Java instrumentation are not supported by the bundled runtime.

In the installed-mod list, **Cross** enables or disables a mod. **Triangle** removes it after confirmation. Disable a recently added mod first when troubleshooting; you can re-enable it later. Changes apply the next time you press Play.

## Install a modpack

1. Go to **Instances → New instance** and choose the Modrinth modpack option.
2. Search for a pack and open its page.
3. Choose **Create instance** and review its installation summary and warnings.
4. Confirm and wait for installation. The pack is created as a separate instance.
5. Select that instance and choose **Play**.

The installer supports compatible Fabric, Quilt, Forge, and NeoForge packs in the launcher's Minecraft version range. If a pack cannot be installed, check its loader, game version, and the reason shown in the dialog. Large PC modpacks can exceed console memory or depend on unsupported features.

## Manage instances and memory

Select an instance to access **Instance settings**, **Clone**, **Rename**, and **Remove**.

| Action | What it does |
| --- | --- |
| **Instance settings** | Change Minecraft memory, graphics memory, and optional JVM or Minecraft arguments. Choose **Save** before leaving; changes apply on Play. |
| **Clone** | Copy mods and configuration. Copying worlds is optional and is off by default. |
| **Rename** | Change the instance's displayed name. |
| **Remove** | Delete a managed instance, including its mods, configuration, and worlds. Back up worlds first. For an imported installation, only its launcher registration is removed; original game files stay in place. |

Start with the default memory settings. Minecraft memory is used by the game; graphics memory is reserved for textures, shaders, and chunk meshes. The launcher limits their combined allocation to **3072 MiB**. Increasing one can leave less room for the other; maximum values are not a universal performance fix.

Leave custom launch arguments empty unless you need a specific setting. The launcher manages memory, account details, game folders, and class paths itself and rejects arguments that would override them.

## Update Cyrene Launcher

1. Close Minecraft and Cyrene Launcher completely.
2. Back up any worlds and instance folders you want to keep.
3. Download the newer `.pkg` from [Releases](https://github.com/CyreneLauncher/CyreneLauncher/releases/latest).
4. Install it over the existing Cyrene Launcher application using your normal package installer.
5. Reopen the launcher and check your accounts and instances.

Updates use the same application identity and preserve existing settings and game data. Keep `/data/orbis-jdk` intact. Install the full launcher package to update its bundled components; you do not need to replace individual graphics libraries.

Java 21 and 25 runtimes are checked for updates when needed. An installed runtime is retained if its update check fails; first-time installation still needs internet access. Offline profiles do not authenticate with online-mode servers. Interrupted mod/modpack and Java runtime downloads keep partial data. Retry the same operation to resume where the server supports it; servers without resume support start that file again. Already verified files are reused, and a checksum mismatch discards the incomplete file before another attempt.

## Back up your worlds

Close the application before copying files with your console's file manager or FTP setup. Managed instances live under:

```text
/data/orbis-jdk/launcher/instances/<instance-id>/game/
```

The instance ID is an internal folder name, not necessarily the displayed name. Inside its game folder:

| Folder | Contents |
| --- | --- |
| `saves/` | Single-player worlds |
| `mods/` | Installed mods |
| `config/` | Mod configuration |
| `logs/` | Minecraft logs |
| `crash-reports/` | Minecraft crash reports, when generated |

Copy the whole instance folder to preserve its setup, or at least `saves/` to preserve worlds. Imported installations keep their existing game location. Offline profile names are stored in launcher settings.

## Troubleshooting

| Problem | What to try |
| --- | --- |
| No game version is available | Check that the configured game-version source is reachable and offers a supported version. |
| Offline profile cannot log in | Enter a valid 1–16 character name using letters, numbers, or underscores, then retry. |
| Download or runtime installation fails | Check internet access and free space, then retry. Java 21/25 must finish downloading before games needing them can launch. |
| Minecraft crashes after adding mods | Disable the most recently added mods, check dependencies, and try an unmodified instance of the same version. |
| A modpack will not install | Read the dialog's reason and check that it uses an offered game version and a supported loader. |
| Settings did not take effect | Open **Instance settings**, choose **Save**, then launch again. |
| Launch returns to the launcher or the application closes | Reopen Cyrene, read any crash summary, and collect the logs below. |
| An older installation behaves unexpectedly after updating | Back up settings and report the issue before replacing files. Older installations can retain custom runner settings. |

### Share a crash log

Select an instance and choose **Share crash log** from its actions. The launcher opens the last crash report, or a game/launcher log if no crash report is available. Review the report with **Up / Down**; **Left / Right** moves a page at a time. Known credentials, chat entries, email addresses, and IP addresses are removed locally, but check for any other personal information before sharing.

Choose **Upload to mclo.gs** to create a shareable log page. Scan the QR code with your phone or copy the displayed link into your bug report. Uploading requires an internet connection and happens only when you choose it. **Circle / Escape** cancels the preview without sending anything.

The reviewed report is also saved at `/data/orbis-jdk/launcher/shared-report.txt`; after a successful upload, the link is saved at `/data/orbis-jdk/launcher/shared-log-url.txt`.

### Report a problem

Open an [issue](https://github.com/CyreneLauncher/CyreneLauncher/issues) and include:

- Cyrene Launcher package version.
- PS4 model (base, Slim, or Pro), firmware, and homebrew environment.
- Minecraft version, loader, and modpack or relevant mods.
- What you did, what you expected, and what happened instead.
- The exact error message and relevant logs.

Useful logs are:

```text
/data/orbis-jdk/launcher/launcher.log
/data/orbis-jdk/logs/orbis-runner.log
/data/orbis-jdk/launcher/instances/<instance-id>/game/logs/latest.log
/data/orbis-jdk/launcher/instances/<instance-id>/game/crash-reports/
```

Share logs as text where possible. Remove personal information or tokens before posting, and never upload the launcher's account-credentials folder.

## For developers

See the [build and release guide](docs/BUILDING.md) for local builds, GitHub Actions, and component releases. [Repository ownership](REPOSITORIES.md) and [package layout](PACKAGING.md) cover the integration details.
