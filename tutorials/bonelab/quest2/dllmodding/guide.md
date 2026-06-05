# 🦴 BONELAB: Comprehensive Quest 2 Code Modding Guide (v63+ Accurate)

*A complete manual for bypassing Meta's v63+ scoped storage restrictions. Because v63 completely breaks LemonLoader's ability to get file permissions natively on the headset, this guide outlines the "Secondary Device" method to patch the IL2CPP build, allowing you to inject Mono assemblies for complex mods like Fusion.*

---

## The v63+ Firmware Problem
As of Meta Quest firmware v63, strict "Scoped Storage" rules not only block on-device file managers, but they completely prevent **LemonLoader** from obtaining the permissions required to decompile and patch the game on the headset. You will be met with a privacy error if you try.

To bypass this, you must extract the game, patch it on a standard Android device (like a phone or an emulator) that allows the permissions, and then sideload the patched version back onto your Quest. 

### 1. Prerequisites
* **PC / Laptop:** For moving files and sideloading.
* **Secondary Android Device:** An Android phone, tablet, or a PC Android emulator (like BlueStacks).
* **Developer Mode:** Enabled on your Quest 2.
* **SideQuest (Advanced Installer):** Installed on your PC.
* **LemonLoader APK:** Downloaded to your PC.

### 2. Backing Up the APK and OBB Files (CRITICAL)
1. Connect your Quest 2 to your PC and allow file access.
2. Open Windows File Explorer and navigate to: `This PC\Quest 2\Internal shared storage\Android\obb\com.StressLevelZero.BONELAB`
3. Copy the entire `com.StressLevelZero.BONELAB` folder to your PC Desktop. This contains the game's massive assets.
4. Open **SideQuest**, go to "Currently Installed Apps," find Bonelab, click the gear icon, and select **Backup APK File**. Save this vanilla APK to your PC.

### 3. Patching via a Secondary Android Device
1. Transfer both the **LemonLoader.apk** and your **Vanilla Bonelab APK** from your PC to your secondary Android phone/tablet.
2. On the phone, install both APKs (you do not need to run Bonelab).
3. Open **LemonLoader** on the phone, select **Bonelab**, and hit **Patch**. The phone's OS will allow the permissions that the Quest blocks.
4. Once patching is complete, use a file manager on the phone (or connect the phone to your PC) to locate and extract the newly **Patched Bonelab APK**. Move this patched APK back to your PC.

### 4. Installing the Patched Game to the Quest
1. Connect your Quest 2 to your PC.
2. In SideQuest, navigate to your installed apps, find Bonelab, and **Uninstall** it. (Don't worry, we backed up the OBB assets).
3. Still in SideQuest, click the "Install APK file from folder" icon at the top, and select the **Patched Bonelab APK** you brought over from your phone.
4. Once installed, **do NOT open the game yet**.

### 5. Restoring the OBB Files
1. In Windows File Explorer, navigate back to `This PC\Quest 2\Internal shared storage\Android\obb\`
2. Drag and drop the `com.StressLevelZero.BONELAB` folder from your Desktop back into the Quest's `obb` folder.

### 6. Generating Directories & Installing Mods (.dlls)
1. Launch Bonelab on the headset. **Wait 5-10 minutes on the black screen.** The Unity assemblies are unhollowing in the background. Close the game once you reach the main menu.
2. Download **BoneLib** and **Bonelab Fusion** from Thunderstore.io to your PC.
3. Navigate to: `This PC\Quest 2\Internal shared storage\Android\data\com.StressLevelZero.BONELABiles`
4. Drag the `.dll` files from the downloaded `Mods` and `Plugins` folders into the newly generated Quest folders.

---

## Networking Setup (FusionHelper)

Because you are using a PC for file management anyway, using **FusionHelper** is the best way to cross-play with PCVR users and maintain lobby stability.
1. Keep your Quest 2 and PC on the same Wi-Fi network.
2. Download and run **FusionHelper** on your PC with Steam running.
3. Click "Log In" on FusionHelper to link your Steam account.
4. Launch Bonelab on your Quest to wirelessly connect and join PCVR Steam lobbies.

*Developer Note: Pushing these unhollowed IL2CPP assemblies on standalone hardware is incredibly taxing. If you plan on capturing complex kinetic scenarios or rendering custom environments for live joke streams, optimizing your setup and expecting minor frame drops during heavy physics calculations is crucial.*