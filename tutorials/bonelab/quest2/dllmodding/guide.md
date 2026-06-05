# 🦴 BONELAB: Comprehensive Quest 2 Code Modding Guide

*A complete manual for patching the IL2CPP build and injecting custom Mono assemblies directly into the standalone Meta Quest 2 environment. This guide covers both the modern PC workaround for newer firmwares and the legacy on-device method.*

---

## Option 1: PC Workaround Method (For v63+ Firmware)
*Recent Meta Quest updates (v63 and beyond) implemented strict "Scoped Storage" rules, blocking on-device file managers. Use this method if your headset is fully updated.*

### 1. Prerequisites
* **PC / Laptop:** For moving files and sideloading.
* **Developer Mode:** Enabled on your Quest 2.
* **SideQuest (Advanced Installer):** Installed on your PC.
* **LemonLoader APK:** Downloaded to your PC.

### 2. Backing Up the OBB Files (CRITICAL)
When LemonLoader patches the game, it requires uninstalling the vanilla APK, which deletes the game's massive `.obb` (texture and asset) files. 
1. Connect your Quest 2 to your PC and allow file access.
2. Navigate to: `This PC\Quest 2\Internal shared storage\Android\obb\com.StressLevelZero.BONELAB`
3. Copy the entire `com.StressLevelZero.BONELAB` folder to your PC Desktop.

### 3. Sideloading LemonLoader and Patching
1. Open **SideQuest** on your PC and install the `LemonLoader.apk` to your headset.
2. Put on the headset, open **LemonLoader** (in *Unknown Sources*).
3. Select **Bonelab** and click **Patch**.
4. **Do NOT click "Restore App"** if Meta prompts you with an unofficial app warning.

### 4. Restoring the OBB Files
1. Reconnect your Quest 2 to your PC.
2. Navigate back to `This PC\Quest 2\Internal shared storage\Android\obb\`
3. Drag and drop the `com.StressLevelZero.BONELAB` folder from your Desktop back into the Quest's `obb` folder.

### 5. Generating Directories & Installing Mods
1. Launch Bonelab on the headset. Wait 5-10 minutes on the black screen while LemonLoader generates Unhollowed Unity assemblies. Close the game once you reach the main menu.
2. Download **BoneLib** and **Bonelab Fusion** from Thunderstore.io.
3. Using Windows File Explorer, navigate to: `This PC\Quest 2\Internal shared storage\Android\data\com.StressLevelZero.BONELABiles`
4. Drag the `.dll` files from the downloaded `Mods` and `Plugins` folders into the corresponding Quest folders.

---

## Option 2: Standalone On-Device Method (Pre-v63 Firmware)
*If you are on an older firmware version (pre-v63) that still allows on-device scoped storage access, you can do this almost entirely without a PC after the initial sideload.*

### 1. Installing & Running LemonLoader
1. **Sideload the APK:** Connect your Quest 2 to your PC, open SideQuest, and install the `LemonLoader.apk`.
2. **Patch the Game Environment:**
    * Open LemonLoader on your Quest 2.
    * Select **Bonelab** and tap **Patch** (takes up to 15 minutes).
    * **Do not click Restore** when prompted by Meta's OS.

### 2. First Boot & Generating Assemblies
1. Launch Bonelab. 
2. Wait 5-10 minutes during the black screen for assembly generation. 
3. Close the game once you reach the menu to initialize the `Mods` and `Plugins` folders.

### 3. Installing BoneLib and Fusion (.dll files)
1. Download BoneLib and Bonelab Fusion from Thunderstore.io (you can do this via the Quest browser).
2. Use an on-device file manager (like Mobile VR Station) to extract the `.zip` files.
3. Move the `.dll` files from the zip's `Mods` and `Plugins` folders directly into the game's `Mods` and `Plugins` folders in `Android/data/com.StressLevelZero.BONELAB/files`.

---

## Networking Guide (Applies to Both Options)

**The Standalone Protocol (Riptide)**
1. Open the **BoneMenu** in Bonelab.
2. Navigate to **Bonelab Fusion** -> **Matchmaking**.
3. Change the protocol to `Riptide` and click **Log In**.

**The PC Bridge (FusionHelper)**
1. Keep your Quest 2 and PC on the same Wi-Fi network.
2. Download and run **FusionHelper** on your PC with Steam running.
3. Click "Log In" on FusionHelper to link your Steam account.
4. Launch Bonelab on your Quest to wirelessly connect and join PCVR Steam lobbies.