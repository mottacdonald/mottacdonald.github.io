# 🦴 BONELAB: Quest 2 Advanced Code Modding & Fusion Guide

*A complete manual for patching the IL2CPP build and injecting custom Mono assemblies directly into the standalone Meta Quest 2 environment.*

---

## 1. The Architecture of Quest Modding

Standard mod.io repositories only allow for SDK-based content (avatars, levels, and static items). To run dynamic, code-executed mods like **BoneLab Fusion**, we must inject `.dll` files directly into the game. Because the Quest 2 runs on Android and the build is compiled via Unity's IL2CPP, a standard PC modloader won't work. Instead, we use **LemonLoader**, an Android-specific fork that patches the APK to accept Mono assembly injection at runtime. 

This deep-level access unlocks full mechanical overhauls, allowing you to orchestrate chaotic multiplayer sessions, set up custom kinetic scenarios, or build unique environments for live joke streams directly on standalone hardware.

## 2. Prerequisites

* **Developer Mode:** Must be enabled on your Meta Quest 2 via the Meta Quest mobile app.
* **SideQuest (or ADB):** Installed on a PC for sideloading the initial patching tool.
* **Fresh Installation:** Ensure Bonelab is updated to the latest patch before beginning.

## 3. Installing & Running LemonLoader

1.  **Download LemonLoader:** Navigate to the official LemonLoader GitHub repository and download the latest `LemonLoader.apk` release.
2.  **Sideload the APK:** Connect your Quest 2 to your PC, open SideQuest, and use the "Install APK file from folder" option to install LemonLoader.
3.  **Patch the Game Environment:**
    * Put on your headset and open LemonLoader (found in your App Library under *Unknown Sources*).
    * Grant the application storage permissions.
    * Select **Bonelab** from the applications list and tap **Patch**. 
    * *Technical Note:* This process decompiles the APK, injects the modloader hooks, and recompiles it. It can take up to 15 minutes.
4.  **Bypass the Restoration Warning:** Once complete, Meta's OS will detect that the app signature has changed and strongly prompt you to "Restore App." **Do not click Restore.** If you do, it will wipe the patched version and reinstall the vanilla build. Select "Open App" or simply close the prompt.

## 4. First Boot & Generating Assemblies

1.  **Launch the Game:** Open Bonelab. 
2.  **Wait for Assembly Generation:** The first boot after patching will take exceptionally long (sometimes 5-10 minutes). During this black screen, LemonLoader is generating the necessary Unity unhollowed assemblies in the background. 
3.  **Initialize Folders:** Once you reach the Bonelab main menu, you can safely close the game. This initial run generates the required `Mods` and `Plugins` directories within the game's Android data folder.

## 5. Installing BoneLib and Fusion (.dll files)

Unlike mod.io SDK mods, code mods are typically hosted on [Thunderstore.io](https://thunderstore.io/c/bonelab/).

1.  Download the required core packages from Thunderstore:
    * **BoneLib:** The foundational library required for almost all code mods.
    * **Bonelab Fusion:** The multiplayer framework itself.
2.  Connect your Quest 2 to your PC and navigate to the internal storage directory:
    `This PC\Quest 2\Internal shared storage\Android\data\com.StressLevelZero.BONELAB\files`
3.  Open your downloaded `.zip` files.
4.  Move the `.dll` files from the zip's `Mods` folder directly into the Quest's `Mods` folder.
5.  Move the `.dll` files from the zip's `Plugins` folder directly into the Quest's `Plugins` folder.

## 6. Configuring Fusion Networking on Standalone

Because the Quest 2 operates independently of the Steamworks API, matchmaking requires a specific protocol setup.

**The Standalone Protocol (Riptide)**
This is the easiest method for purely standalone, PC-free multiplayer.
1.  Launch Bonelab and open the **BoneMenu** (found in your radial Preferences menu).
2.  Navigate to **Bonelab Fusion** -> **Matchmaking**.
3.  Change the networking protocol from `Steam` (the default) to `Riptide`.
4.  Click **Log In**. It will authenticate seamlessly using your Meta Quest username.
5.  You can now browse public lobbies or host your own directly from the headset.

**The PC Bridge (FusionHelper)**
If you need to cross-play with PCVR users relying on Steam's network:
1.  Keep your Quest 2 connected to the same local Wi-Fi network as your PC.
2.  Download and run **FusionHelper** on your PC.
3.  Click "Log In" on the FusionHelper terminal to link your Steam account. It acts as a local relay, bridging the headset's traffic through the PC's Steam networking layer.

---
*Performance Tip: Keep in mind that hosting a heavily populated Fusion lobby on standalone hardware will push the headset to its limits. If you are capturing footage for YouTube or running a stream, expect minor frame drops during intensive physics calculations or when rendering multiple custom avatars simultaneously.*
