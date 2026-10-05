# Meridian Global Enterprises — Approved Knowledge Base
## IT Support Agent Retrieval Source (Phase 1)

**Classification:** Internal — approved Meridian KB  
**Language:** English only  
**Usage:** This document is the sole technical resolution source for the Meridian AEX agent. Retrieve at most **three** ranked articles per issue. Do not invent steps that are not in an article.

**How to search this KB (for the agent after PDF indexing):**
1. Identify Domain first: Hardware | Network | Applications | Access Management | Service Catalogue.
2. Search with user symptoms + application/device names + exact error text.
3. Rank by keyword overlap and symptom match. Present **Attempt 1** (best match), then **Attempt 2**, then **Attempt 3**.
4. Each article below starts with `KB-ID`, Domain, Category, Keywords, Symptoms, Resolution, Verify, If unresolved.
5. Password/credential reset articles instruct **escalation**. Never reset or reveal passwords.

---

# Domain: Hardware

## KB-HW-001 — Laptop or Desktop Will Not Power On
**Domain:** Hardware  
**Category:** End-user device  
**Keywords:** no power, won't turn on, dead laptop, blank, not starting, no lights  
**Symptoms:** Device does not start; no LED; no fan; screen stays black after power button.

**Resolution:**
1. Confirm the power adapter LED is on and the cable is fully seated in the laptop and wall outlet. Try a different known-good outlet.
2. Remove any docking station or USB-C hub. Connect the charger directly to the device.
3. Hold the power button for 15 seconds to discharge residual power, then press power once.
4. If a removable battery exists, disconnect AC, remove the battery, hold power 15 seconds, refit battery, connect AC, power on.
5. Check for any faint LED (charging amber/white). If charging LED is off with a known-good charger, the adapter or port may be faulty.

**Verify:** Device boots to the Meridian login screen.  
**If unresolved:** Raise an Incident (Hardware / Power). Offer catalogue item “Request replacement charger” if the adapter is suspected. Do not open the chassis.

---

## KB-HW-002 — Laptop Is Slow or Unresponsive
**Domain:** Hardware  
**Category:** Performance  
**Keywords:** slow laptop, lag, freeze, high CPU, spinning, taking long to open  
**Symptoms:** Applications take a long time to open; mouse stutters; disk or CPU appears constantly busy.

**Resolution:**
1. Restart the device and wait until the login screen is fully ready before opening applications.
2. Close unused browsers and applications. In Task Manager, note any process consistently above 80% CPU (do not kill security or system processes).
3. Confirm at least 15% free disk space on the system drive. Empty Recycle Bin and Downloads of obviously large unused files.
4. Disconnect unused USB devices and test off the docking station.
5. Install pending Windows and Meridian-managed software updates, then restart.

**Verify:** Device remains usable for 10 minutes of normal work.  
**If unresolved:** Incident (Hardware / Performance). Capture approximate free disk space and whether a docking station is in use.

---

## KB-HW-003 — Blue Screen or Unexpected Restart
**Domain:** Hardware  
**Category:** Stability  
**Keywords:** BSOD, blue screen, crash, restart loop, stop code, unexpected shutdown  
**Symptoms:** Windows stops with a blue screen or reboots without warning.

**Resolution:**
1. Note the stop code or any error text shown (for example, DRIVER_IRQL, MEMORY_MANAGEMENT).
2. Remove newly added USB devices, docks, and external GPUs/adapters. Boot with only power, keyboard, mouse.
3. Boot normally and check Windows Update for pending driver or cumulative updates. Install and restart.
4. Run the Windows Memory Diagnostic from Windows Security / Recovery options if the stop code mentions memory.
5. If crashes started after a specific docking station or docking firmware change, test undocked.

**Verify:** Device stays up through a restart and 15 minutes of work.  
**If unresolved:** Incident (Hardware / Stability) including the stop code. Do not advise registry edits or unsupported boot flags.

---

## KB-HW-004 — Keyboard, Mouse, or Touchpad Not Working
**Domain:** Hardware  
**Category:** Peripherals  
**Keywords:** keyboard dead, mouse not working, touchpad, keys stuck, cursor  
**Symptoms:** Keys do not type; cursor does not move; only some keys fail.

**Resolution:**
1. For USB devices: unplug, wait 10 seconds, try another USB port, avoid unpowered hubs.
2. For wireless: replace batteries; toggle the device power switch; re-pair using the vendor receiver only.
3. Touchpad: check the function-key toggle (often Fn+F something) and Windows Settings → Bluetooth & devices → Touchpad is On.
4. Restart the PC. Test in an on-screen keyboard if physical keys fail.
5. If an external keyboard works and the built-in one does not, treat as hardware fault.

**Verify:** Typing and cursor movement work in Notepad.  
**If unresolved:** Incident (Hardware / Peripherals). Catalogue: “Request USB keyboard/mouse”.

---

## KB-HW-005 — Monitor or External Display Has No Image
**Domain:** Hardware  
**Category:** Display  
**Keywords:** no display, blank monitor, second screen, HDMI, DisplayPort, dock screen  
**Symptoms:** Laptop lid works but external monitor is black, or all screens black.

**Resolution:**
1. Confirm the monitor power LED is on. Try the monitor’s input button (HDMI / DisplayPort / USB-C).
2. Reseat the video cable at both ends. Test a known-good cable if available.
3. Press Windows+P and select Duplicate or Extend. Wait 5 seconds.
4. Disconnect the dock, connect the monitor directly to the laptop if the laptop has a video port.
5. In Display settings, click Detect. Set the correct resolution for the monitor.

**Verify:** Image appears on the intended screen and Windows sees the display.  
**If unresolved:** Incident (Hardware / Display). Catalogue: “Request additional monitor” if the user needs a new screen rather than a fault.

---

## KB-HW-006 — Printer Will Not Print
**Domain:** Hardware  
**Category:** Printing  
**Keywords:** printer, not printing, queue stuck, offline printer, toner, paper jam  
**Symptoms:** Jobs sit in the queue; printer shows offline; no output.

**Resolution:**
1. Confirm the printer is powered, has paper, and shows no jam/toner warnings on its panel.
2. On the PC, Settings → Bluetooth & devices → Printers. Remove a stuck job (Open queue → Cancel all). Set the printer Online.
3. Print a Windows test page. If test page works, retry the original application.
4. For network printers, confirm the user is on Meridian network or VPN. Restart the PC print spooler via restart if the queue remains stuck after clearing jobs.
5. Re-add the printer from the Meridian approved printer list. Do not install random vendor packages from the internet.

**Verify:** A one-page test document prints.  
**If unresolved:** Incident (Hardware / Printing) with printer name and location.

---

## KB-HW-007 — Docking Station Not Detecting Devices
**Domain:** Hardware  
**Category:** Docking  
**Keywords:** dock, docking station, USB-C dock, ports dead, monitors via dock  
**Symptoms:** Laptop charges on dock but USB, Ethernet, or monitors do not work.

**Resolution:**
1. Use the original dock cable in the laptop USB-C/Thunderbolt port marked for data/display, not charge-only accessories.
2. Disconnect the dock, wait 20 seconds, reconnect. Power-cycle the dock if it has a power brick.
3. Test one monitor and one USB device at a time.
4. Update Meridian-managed dock/firmware updates if offered in Company Portal / Software Center.
5. Test the same laptop with a colleague’s known-good dock of the same model, or the user’s dock with another laptop.

**Verify:** Network or USB device and at least one display work through the dock.  
**If unresolved:** Incident (Hardware / Docking).

---

## KB-HW-008 — Battery Drains Quickly or Will Not Charge
**Domain:** Hardware  
**Category:** Power  
**Keywords:** battery drain, not charging, 0%, plugged in not charging, battery health  
**Symptoms:** Charge percentage falls fast; stays on 0%; “plugged in, not charging”.

**Resolution:**
1. Confirm genuine Meridian-issued charger wattage for the model (undersized chargers often show “not charging” under load).
2. Close high-draw apps and reduce brightness. Test charging with lid closed vs open.
3. Remove the dock and charge directly.
4. Restart. In Windows, check Power & battery for battery saver and unusual app usage.
5. If the battery is swollen, stop using the device and escalate as hardware safety — do not press on the palm rest.

**Verify:** Percentage increases while idle on AC.  
**If unresolved:** Incident (Hardware / Battery). Catalogue: replacement charger if adapter suspected.

---

## KB-HW-009 — Webcam, Microphone, or Speakers Not Working
**Domain:** Hardware  
**Category:** Audio/Video  
**Keywords:** webcam, camera, mic, microphone, speakers, no sound, Teams camera  
**Symptoms:** Camera black in meetings; others cannot hear the user; no playback.

**Resolution:**
1. Confirm the privacy shutter is open. Fn camera-mute keys must be off.
2. Windows Settings → Privacy → Camera / Microphone: allow desktop apps and Microsoft Teams / browser.
3. Sound settings: select the correct playback and recording device (headset vs laptop). Disable exclusive mode conflicts by choosing the headset explicitly.
4. Unplug and replug the headset. Try a different USB port. Test in Voice Recorder and Camera app before Teams.
5. Restart the PC. If only Teams fails, see KB-APP-002.

**Verify:** Camera preview shows video; mic level moves when speaking; speakers play a test sound.  
**If unresolved:** Incident (Hardware / Audio-Video). Catalogue: “Request headset”.

---

## KB-HW-010 — USB Device Not Recognised
**Domain:** Hardware  
**Category:** Peripherals  
**Keywords:** USB not recognised, unknown device, flash drive, code 43, port  
**Symptoms:** Device does not appear in Explorer; Windows reports unknown USB device.

**Resolution:**
1. Try a different port on the laptop itself (not the dock). Avoid unpowered hubs.
2. For storage devices, wait 20 seconds; check Disk Management only to see if a drive letter is missing — do not format the drive.
3. Restart with the device disconnected, then connect after login.
4. Test the device on another Meridian PC if available.
5. Encrypted or personal storage must follow Meridian DLP policy; do not instruct users to disable security software.

**Verify:** Device appears and opens in File Explorer.  
**If unresolved:** Incident (Hardware / USB).

---

## KB-HW-011 — Device Overheating or Loud Fan
**Domain:** Hardware  
**Category:** Thermal  
**Keywords:** hot laptop, fan loud, overheating, shutdown heat, burning smell  
**Symptoms:** Chassis is very hot; fans run constantly; device throttles or shuts down.

**Resolution:**
1. Place the device on a hard flat surface. Do not block vents. Remove thick cases while under load.
2. Close unused apps and browser tabs. Pause large downloads/sync if possible.
3. Check air vents for dust obstruction. Do not use liquids or compressed air inside the chassis unless Facilities/IT hardware process allows it — end users should not open the case.
4. Update Meridian-managed BIOS/firmware if offered.
5. If there is a burning smell or visible damage, power off immediately and raise a high-urgency Incident.

**Verify:** Temperature and fan noise drop after idle on a hard surface.  
**If unresolved:** Incident (Hardware / Thermal).

---

## KB-HW-012 — Damaged Screen, Hinge, or Chassis
**Domain:** Hardware  
**Category:** Break/fix  
**Keywords:** cracked screen, broken hinge, spilled liquid, damaged laptop  
**Symptoms:** Visible physical damage; liquid spill; image lines; hinge loose.

**Resolution:**
1. For liquid spills: power off immediately, disconnect AC, do not turn on again. Raise Incident as Hardware / Liquid damage.
2. For cracked screens: use an external monitor if the device still boots (KB-HW-005) and raise Incident for repair/replace.
3. Do not attempt glass removal, hinge screws, or third-party repair.
4. Back up work to OneDrive/SharePoint if the device still works.

**Verify:** Not applicable — this is a break/fix path.  
**If unresolved:** Always Incident (Hardware / Break-fix). Catalogue: “Request new laptop” only if fulfilment confirms replacement rather than repair.

---

# Domain: Network

## KB-NET-001 — No Internet on Office Wi-Fi
**Domain:** Network  
**Category:** Wireless  
**Keywords:** no internet, wifi, wi-fi, wireless, can't connect, SSID, meridianguest  
**Symptoms:** Wi-Fi shows connected but sites do not load, or SSID is missing.

**Resolution:**
1. Confirm the user is on the corporate SSID, not a guest or personal hotspot, unless they are a visitor on guest Wi-Fi.
2. Toggle Wi-Fi off and on. Forget the SSID and reconnect with Meridian credentials as instructed on the office network card.
3. Move closer to an access point. Disable VPN temporarily to test (see KB-NET-002 if only corporate apps fail).
4. Restart the PC. Open a browser to a public status page and an internal portal.
5. Check airplane mode is off. Forget unused conflicting SSIDs.

**Verify:** Internal portal and an external HTTPS site both load.  
**If unresolved:** Incident (Network / Wireless) with building/floor.

---

## KB-NET-002 — VPN Will Not Connect
**Domain:** Network  
**Category:** Remote access  
**Keywords:** VPN, AnyConnect, GlobalProtect, tunnel, VPN timeout, not connecting  
**Symptoms:** VPN client fails to connect; timeout; authentication error; connected but no internal resources.

**Resolution:**
1. Confirm internet works without VPN (browser to a public site).
2. Use the official Meridian VPN client only. Disconnect other VPNs.
3. Retry with username in the approved format (usually corporate email). If MFA push appears, approve it on the registered device.
4. Restart the VPN client, then the PC. Try an alternate VPN gateway if the client lists more than one.
5. If the VPN connects but file shares or internal apps fail, disconnect/reconnect once and test DNS by opening the intranet URL (not by running diagnostic scans).

**Verify:** VPN status is Connected and intranet loads.  
**If unresolved:** If password/MFA is the failure, follow Access articles and escalate credential resets. Otherwise Incident (Network / VPN). Catalogue: “Request VPN access” for users who never had VPN entitlement.

---

## KB-NET-003 — Internet Is Very Slow
**Domain:** Network  
**Category:** Performance  
**Keywords:** slow wifi, slow internet, buffering, high latency, teams lag network  
**Symptoms:** Pages crawl; calls pixelate; large files stall. Other devices on the same network may be fine.

**Resolution:**
1. Test with VPN disconnected and connected. If only VPN is slow, reconnect to a different gateway (KB-NET-002).
2. Move closer to the AP; switch from 2.4 GHz guest networks to corporate SSID.
3. Pause large OneDrive/sync and cloud backups temporarily.
4. Restart the PC and, if at home, the home router (power off 30 seconds) — only the user’s own router.
5. Try a wired dock Ethernet if available.

**Verify:** Intranet and a sample file open in a reasonable time.  
**If unresolved:** Incident (Network / Performance) with location (office/home) and VPN on/off result.

---

## KB-NET-004 — Wired Ethernet Not Working
**Domain:** Network  
**Category:** Wired  
**Keywords:** ethernet, LAN, cable, dock network, no network cable  
**Symptoms:** Cable connected but no network; yellow bang on adapter.

**Resolution:**
1. Reseat the cable at PC/dock and wall/switch. Try a known-good cable.
2. Disable Wi-Fi temporarily to avoid split routing confusion.
3. Unplug dock Ethernet, connect a USB-C/USB Ethernet adapter or wall cable directly if available.
4. Restart PC. Confirm the adapter is enabled in Windows network adapters list.
5. Office wall ports that never worked for anyone should be reported with room and port label.

**Verify:** IP is obtained and intranet loads on wire.  
**If unresolved:** Incident (Network / Wired) with room/port.

---

## KB-NET-005 — Cannot Reach Shared Drive or File Server
**Domain:** Network  
**Category:** File access  
**Keywords:** shared drive, mapped drive, \\\\server, access denied share, network path  
**Symptoms:** Mapped drive disconnects; path not found; access denied.

**Resolution:**
1. Confirm VPN is connected if the user is off-site.
2. Use the full approved path from the service catalogue / intranet, not a remembered letter only.
3. Restart the PC after VPN connect, then retry the path.
4. Access denied with a valid path is usually permissions — go to KB-ACC-006. Path not found after VPN is network/name resolution — retry VPN.
5. Do not instruct users to disable firewalls.

**Verify:** The share opens and the user can open a file they already own.  
**If unresolved:** Incident (Network / File share) or Access request if permissions.

---

## KB-NET-006 — DNS or “Site Cannot Be Reached” for Internal URLs
**Domain:** Network  
**Category:** Name resolution  
**Keywords:** DNS, intranet not loading, server not found, cannot resolve, proxy  
**Symptoms:** Public sites work; Meridian intranet and apps fail, or the reverse through proxy.

**Resolution:**
1. If off-site, connect VPN first, then retry internal URLs.
2. Try the intranet homepage vs a bookmark that may be outdated.
3. Restart the PC. Flush is not required if a restart is done.
4. Confirm proxy/autoconfig is the Meridian default (do not set arbitrary proxy IPs).
5. Test in a private browser window to rule out a bad cached redirect.

**Verify:** Intranet homepage loads.  
**If unresolved:** Incident (Network / DNS).

---

## KB-NET-007 — Conference Room or Meeting Room Network Issues
**Domain:** Network  
**Category:** Meeting rooms  
**Keywords:** conference room, room PC, room wifi, calendar room, huddle  
**Symptoms:** Room PC offline; guests cannot join Wi-Fi; room display has no network.

**Resolution:**
1. Restart the room PC and the display. Confirm HDMI/USB from the room PC is selected.
2. Guests should use Meridian Guest Wi-Fi per the posted room card — not the corporate SSID.
3. If the room calendar panel is offline, note the room name and floor for Facilities/IT — this is still IT Network if the panel is an IT device.
4. Do not reconfigure the room switch or wireless controller.

**Verify:** Room PC reaches Teams/Zoom and the calendar shows meetings.  
**If unresolved:** Incident (Network / Meeting room) with building and room name.

---

## KB-NET-008 — Home Network Works but Corporate Apps Do Not
**Domain:** Network  
**Category:** Remote access  
**Keywords:** home wifi works, outlook fails offsite, intranet fail, split tunnel  
**Symptoms:** YouTube works; Outlook, intranet, or HR portal does not.

**Resolution:**
1. Connect VPN (KB-NET-002). Retry the corporate app.
2. Confirm MFA is not blocking the app (KB-ACC-003).
3. Restart Outlook/Teams after VPN is connected.
4. If only one app fails with VPN up, switch to the Applications domain articles.

**Verify:** Intranet plus the failing app both open on VPN.  
**If unresolved:** Incident (Network / Remote apps).

---

# Domain: Applications

## KB-APP-001 — Microsoft Outlook Not Opening or Not Syncing
**Domain:** Applications  
**Category:** Email  
**Keywords:** outlook, mail, not opening, stuck, not receiving mail, OST, profile  
**Symptoms:** Outlook hangs on splash; mailbox not updating; send stuck in Outbox.

**Resolution:**
1. Confirm internet/VPN as required. Close Outlook fully and reopen.
2. Check Outlook Web (browser) with the same mailbox. If web works, the issue is the desktop client.
3. Disable hardware acceleration in Outlook options if the window is blank (if the user can open Options).
4. Create a new Outlook profile from Control Panel → Mail only if web mail works and the desktop profile is corrupt. Do not delete the mailbox on the server.
5. For send failures, check the recipient address and attachment size against the 25 MB guidance.

**Verify:** Inbox updates and a test mail to self arrives.  
**If unresolved:** Incident (Applications / Outlook).

---

## KB-APP-002 — Microsoft Teams Meetings — Audio, Video, or Sign-in
**Domain:** Applications  
**Category:** Collaboration  
**Keywords:** teams, meeting, no audio, echo, camera teams, teams login, dark screen  
**Symptoms:** Cannot join; no mic/camera; sign-in loop.

**Resolution:**
1. Use the official Teams app. Sign out and sign in with corporate credentials.
2. Select the correct speaker/mic/camera in Teams Settings → Devices. Run the Teams device test call.
3. Apply KB-HW-009 if devices fail in Camera/Voice Recorder as well.
4. Clear the Teams cache only by fully exiting Teams (tray icon) and renaming the cache folder under the user’s AppData Teams directory to Teams.bak, then restart Teams — do not delete OneDrive data.
5. If the meeting policy blocks guest join, the organiser must admit the user or use the calendar join link.

**Verify:** Test call plays audio and camera preview works.  
**If unresolved:** Incident (Applications / Teams).

---

## KB-APP-003 — Microsoft 365 Apps Need Activation or Show Errors
**Domain:** Applications  
**Category:** Office  
**Keywords:** office activation, unlicensed product, word excel, 365, product deactivated  
**Symptoms:** Yellow unlicensed bar; cannot save; activation prompts.

**Resolution:**
1. Sign in to Office with the corporate account, not a personal Microsoft account.
2. Close all Office apps. Open Word and complete activation.
3. Confirm the user has an M365 licence. If never licensed, this is a Service Request (catalogue: “Request Microsoft 365 licence”), not an Incident.
4. Restart the PC after sign-in.

**Verify:** Word shows Licensed and can save a document to OneDrive.  
**If unresolved:** Incident (Applications / Office) if licence exists; otherwise Service Request.

---

## KB-APP-004 — Web Browser Crashes or Cannot Open Required Sites
**Domain:** Applications  
**Category:** Browser  
**Keywords:** chrome crash, edge hang, site blocked, certificate warning, cookies  
**Symptoms:** Browser closes; one business site fails; certificate warnings.

**Symptoms detail:** Corporate SSO sites may fail in a non-approved browser.

**Resolution:**
1. Use Microsoft Edge or the Meridian-approved Chrome. Update the browser from Company Portal.
2. Retry in InPrivate/Incognito.
3. Clear cached data for the specific site only if InPrivate works.
4. Certificate warnings on true Meridian HTTPS sites: do not bypass casually if the name does not match — raise Incident (Applications / Browser).
5. Pop-up blockers may block SSO — allow pop-ups for the login domain.

**Verify:** The required site completes login.  
**If unresolved:** Incident (Applications / Browser) with the exact URL and error text.

---

## KB-APP-005 — Line-of-Business Application Will Not Start or Errors on Launch
**Domain:** Applications  
**Category:** LOB  
**Keywords:** SAP, CRM, ERP, business app, launch error, runtime error, executable  
**Symptoms:** App crashes at splash; missing DLL; licence error; timeout to server.

**Resolution:**
1. Confirm VPN if the app is internal. Confirm the user previously had working access.
2. Restart the PC. Launch from the official shortcut, not a copied EXE.
3. Install pending updates from Company Portal / Software Center for that app.
4. If “access denied” or no role in the app, switch to Access Management (KB-ACC-004).
5. Capture the exact error message and screenshot for the ticket if still failing.

**Verify:** App reaches the home screen.  
**If unresolved:** Incident (Applications / LOB) with application name and error text.

---

## KB-APP-006 — Application Freezes During Use
**Domain:** Applications  
**Category:** Stability  
**Keywords:** freeze, not responding, hang, spinner, crash while working  
**Symptoms:** App title bar shows Not Responding.

**Resolution:**
1. Wait 60 seconds. Save work in other apps.
2. If only one document causes the freeze, the file may be corrupt — try a copy or export.
3. Repair Office or the app from Settings → Apps → Modify/Repair when that option exists.
4. Restart PC. Disable unnecessary COM add-ins in Outlook/Excel if the freeze is add-in related and the user can access Options.

**Verify:** The same workflow completes once.  
**If unresolved:** Incident (Applications / Stability).

---

## KB-APP-007 — Software Install or Update Failed
**Domain:** Applications  
**Category:** Deployment  
**Keywords:** install failed, company portal, software center, update error, MSI  
**Symptoms:** Company Portal error; install stuck; update rolls back.

**Resolution:**
1. Restart PC and retry the install from Company Portal / Software Center only.
2. Confirm disk space (KB-HW-002). Close the app being updated.
3. If the title is not in the catalogue, the user must request it (Service Catalogue — software install) rather than sideloading.
4. Do not download installers from the public internet.

**Verify:** App appears in the Start menu and opens.  
**If unresolved:** Incident (Applications / Deployment) if the approved package fails; Service Request if the package is not assigned.

---

## KB-APP-008 — PDF or File Will Not Open
**Domain:** Applications  
**Category:** Files  
**Keywords:** PDF, adobe, file corrupt, access denied file, OneDrive sync  
**Symptoms:** File prompts for app; error opening; OneDrive cloud icon stuck.

**Resolution:**
1. Confirm OneDrive is synced (cloud icon). Open from File Explorer after sync completes.
2. Use Edge or Adobe from Company Portal for PDFs.
3. If Access Denied, it is permissions (KB-ACC-006).
4. If the file is corrupt, restore a previous OneDrive version from the web portal.

**Verify:** File opens and is readable.  
**If unresolved:** Incident (Applications / Files).

---

## KB-APP-009 — OneDrive or SharePoint Sync Problems
**Domain:** Applications  
**Category:** Collaboration  
**Keywords:** OneDrive, SharePoint, sync pending, files on-demand, quota  
**Symptoms:** Files stuck on sync; missing folders; quota full.

**Resolution:**
1. Click the OneDrive cloud icon → pause and resume sync. Sign out/in if credentials expired.
2. Check storage quota. If full, the user must delete or archive — or request more storage via catalogue if offered.
3. Confirm VPN is not required for SharePoint (usually internet is enough). If SSO fails, Access articles.
4. Move out of invalid Windows path length by shortening folder names if the client reports path too long.

**Verify:** A test file appears on another device or the web portal.  
**If unresolved:** Incident (Applications / OneDrive).

---

## KB-APP-010 — MFA Prompt on Application but User Cannot Complete It
**Domain:** Applications  
**Category:** Authentication  
**Keywords:** MFA app, authenticator, prompt loop, teams MFA, office MFA  
**Symptoms:** App waits on MFA; user has no push; number matching fails.

**Resolution:** Follow KB-ACC-003. Do not provide bypass codes.  
**If unresolved:** Escalate to Agent Assist (security-sensitive). Catalogue: “Request MFA device reset” as Service Request after human verification.

---

# Domain: Access Management

## KB-ACC-001 — Account Locked
**Domain:** Access Management  
**Category:** Account  
**Keywords:** account locked, locked out, too many attempts, cannot login windows  
**Symptoms:** Windows or SSO says the account is locked.

**Resolution:**
1. Confirm the user is using the corporate ID (usually email) and correct MFA device.
2. Wait 15 minutes for an automatic unlock if Meridian policy allows it, then retry once.
3. The agent **cannot** unlock accounts or reset passwords. Offer Agent Assist immediately if the user cannot wait or lock repeats.
4. After unlock (by a human), advise a single careful password entry; excessive retries re-lock the account.

**Verify:** Interactive login succeeds.  
**If unresolved:** Mandatory Agent Assist. Optionally log an Incident (Access / Lockout) if no human is available.

---

## KB-ACC-002 — Password Expired or Forgotten
**Domain:** Access Management  
**Category:** Credentials  
**Keywords:** password expired, forgot password, reset password, change password  
**Symptoms:** Forced password change; user does not know the password.

**Resolution:**
1. If the user still knows the current password and Windows prompts a change, complete the on-screen change with Meridian complexity rules (length and complexity as shown on the form). Do not invent a password for the user.
2. If the password is unknown, **do not reset it**. Escalate to Agent Assist.
3. Never ask the user to send a password in chat. Never generate a temporary password in chat.

**Verify:** User signs in after a self-service change.  
**If unresolved:** Mandatory Agent Assist.

---

## KB-ACC-003 — MFA / Authenticator Not Working
**Domain:** Access Management  
**Category:** MFA  
**Keywords:** MFA, 2FA, authenticator, SMS code, push notification, number matching  
**Symptoms:** No push; lost phone; new phone; codes rejected.

**Resolution:**
1. Confirm the phone has internet and notifications enabled for the authenticator app.
2. Open the authenticator app and wait for the prompt; use number matching exactly.
3. If the phone was replaced or the app was uninstalled, the agent cannot re-enrol MFA. Escalate to Agent Assist.
4. Do not disable MFA.

**Verify:** One successful MFA challenge on Outlook Web or VPN.  
**If unresolved:** Mandatory Agent Assist. Service Request “MFA reset” after human verification.

---

## KB-ACC-004 — Need Access to an Application
**Domain:** Access Management  
**Category:** Entitlement  
**Keywords:** access request, role, licence, cannot see app, permission application  
**Symptoms:** App opens but no role; app missing from portal; licence missing.

**Resolution:**
1. This is a **Service Request**, not an Incident, unless the user had access yesterday and it was removed unexpectedly.
2. Recommend the catalogue item that matches the application (see Catalogue FAQs).
3. If sudden loss of existing access, search KB once more, then Incident (Access / Entitlement loss) after confirmation.

**Verify:** Catalogue item is recommended with a one-line reason.  
**If unresolved:** Service Request or Agent Assist.

---

## KB-ACC-005 — Shared Mailbox or Distribution List Access
**Domain:** Access Management  
**Category:** Messaging access  
**Keywords:** shared mailbox, distribution list, DL, send as, mailbox permission  
**Symptoms:** Mailbox missing in Outlook; cannot send as DL.

**Resolution:**
1. If the user never had the mailbox, raise a Service Request (catalogue: shared mailbox access).
2. If recently granted, restart Outlook and wait up to 60 minutes for directory replication, then reopen Outlook.
3. Open File → Account Settings → Change → More Settings → Advanced → Add the mailbox if policy uses explicit mapping.
4. Do not grant permissions via PowerShell.

**Verify:** Mailbox appears in the left folder pane.  
**If unresolved:** Service Request if new; Incident if previously working.

---

## KB-ACC-006 — File Share or SharePoint Permissions
**Domain:** Access Management  
**Category:** Data access  
**Keywords:** access denied folder, sharepoint permission, cannot edit, request access  
**Symptoms:** User can see a link but not open or edit.

**Resolution:**
1. Use SharePoint “Request access” if shown — that is the official path.
2. Confirm the user is in the correct group (they will not see group names; ask who the site owner is).
3. Off-site users must use VPN only if the library is internal-only (KB-NET-005).
4. Recommend catalogue “File share / SharePoint access request” with the site URL.

**Verify:** After fulfilment, file opens. The agent does not grant access itself.  
**If unresolved:** Service Request.

---

## KB-ACC-007 — New Joiner Cannot Access Standard Tools
**Domain:** Access Management  
**Category:** Joiner  
**Keywords:** new starter, new joiner, first day, no email, no laptop account  
**Symptoms:** Brand-new employee missing mailbox, VPN, or laptop login.

**Resolution:**
1. Confirm the user ID entered at chat start is the joiner’s own ID.
2. Standard joiner tooling is catalogue-driven: laptop, M365, VPN, badge is Facilities (out of scope unless IT).
3. Recommend “New joiner IT bundle” if present; otherwise individual catalogue items.
4. Do not create accounts manually.

**Verify:** Catalogue recommendations listed.  
**If unresolved:** Service Request plus Agent Assist if the joiner is blocked on day one.

---

## KB-ACC-008 — Privileged or Admin Access Request
**Domain:** Access Management  
**Category:** Privileged  
**Keywords:** local admin, privileged, admin rights, sudo, elevation  
**Symptoms:** User wants administrator rights on the PC or a server.

**Resolution:**
1. Out of standard self-service. Recommend catalogue “Privileged access request” if it exists.
2. If no catalogue item, escalate to Agent Assist. Do not provide workarounds that bypass UAC or security tools.

**Verify:** Request logged or human engaged.  
**If unresolved:** Agent Assist.

---

## KB-ACC-009 — VPN Account Not Entitled
**Domain:** Access Management  
**Category:** Remote access entitlement  
**Keywords:** VPN access request, not authorised VPN, no vpn token  
**Symptoms:** VPN client installed but authorisation failed.

**Resolution:**
1. Distinguish from KB-NET-002 (technical tunnel failure). “Not authorised” / “no entitlement” is Access.
2. Recommend catalogue “Request VPN access”.
3. After fulfilment, user must wait for directory update, then reconnect.

**Verify:** Catalogue recommendation given.  
**If unresolved:** Service Request.

---

# Domain: Service Catalogue FAQs

## KB-CAT-001 — When to Use Incident vs Service Request
**Domain:** Service Catalogue  
**Category:** FAQ  
**Keywords:** incident vs request, something broken, I need a new, catalogue  
**Guidance:**
- Incident: something that used to work is broken, degraded, or unavailable.
- Service Request: user wants something new (software, hardware, access, information).
- If unclear, ask: “Is something broken, or are you requesting something new?”

---

## KB-CAT-002 — Request Software Installation
**Domain:** Service Catalogue  
**Category:** Software  
**Keywords:** install software, request app, visio, project, adobe, chrome  
**Catalogue item:** Request software installation  
**Why:** New software is fulfilled from the approved catalogue, not by ad-hoc download.  
**Link placeholder:** https://meridiandesk.internal/catalog/software-install  
**User must provide:** Software name, business justification, manager if required by the form.

---

## KB-CAT-003 — Request VPN Access
**Domain:** Service Catalogue  
**Category:** Access  
**Keywords:** request vpn, remote access, work from home access  
**Catalogue item:** Request VPN access  
**Why:** VPN entitlement is granted through Identity, not by installing a client alone.  
**Link placeholder:** https://meridiandesk.internal/catalog/vpn-access  

---

## KB-CAT-004 — Request a New Laptop or Replacement Device
**Domain:** Service Catalogue  
**Category:** Hardware  
**Keywords:** new laptop, replacement laptop, refresh, order computer  
**Catalogue item:** Request new laptop  
**Why:** Device issuance is a catalogue fulfilment process. Broken devices still need an Incident first (KB-HW-012); replacement is decided by fulfilment.  
**Link placeholder:** https://meridiandesk.internal/catalog/new-laptop  

---

## KB-CAT-005 — Request Shared Mailbox
**Domain:** Service Catalogue  
**Category:** Messaging  
**Keywords:** shared mailbox request, team inbox, generic email  
**Catalogue item:** Request shared mailbox  
**Why:** Mailboxes are provisioned with an owner and permissions.  
**Link placeholder:** https://meridiandesk.internal/catalog/shared-mailbox  
**User must provide:** Mailbox display name, owners, members, purpose.

---

## KB-CAT-006 — Request Additional Monitor, Headset, or Keyboard
**Domain:** Service Catalogue  
**Category:** Peripherals  
**Keywords:** extra monitor, headset, keyboard, mouse, webcam request  
**Catalogue item:** Request IT peripheral  
**Why:** Standard peripherals are stocked items.  
**Link placeholder:** https://meridiandesk.internal/catalog/peripherals  

---

## KB-CAT-007 — Request Microsoft 365 or Other Licence
**Domain:** Service Catalogue  
**Category:** Licence  
**Keywords:** visio licence, project licence, 365 licence, unlicensed  
**Catalogue item:** Request software licence  
**Why:** Licence assignment is entitlement, not a break/fix.  
**Link placeholder:** https://meridiandesk.internal/catalog/licence  

---

## KB-CAT-008 — Request File Share or SharePoint Site Access
**Domain:** Service Catalogue  
**Category:** Data  
**Keywords:** access to folder, sharepoint site access, project drive  
**Catalogue item:** Request file or SharePoint access  
**Why:** Permissions are granted by the data owner through a request.  
**Link placeholder:** https://meridiandesk.internal/catalog/data-access  
**User must provide:** URL or share path, access level (read/edit), owner name.

---

## KB-CAT-009 — Request MFA Reset (Human Fulfilment)
**Domain:** Service Catalogue  
**Category:** Identity  
**Keywords:** reset MFA, new phone authenticator, lost phone  
**Catalogue item:** Request MFA reset  
**Why:** Identity proofing is required. The chat agent must escalate or raise the request only after explaining a human will verify identity.  
**Link placeholder:** https://meridiandesk.internal/catalog/mfa-reset  

---

## KB-CAT-010 — Browse All Common Catalogue Items
**Domain:** Service Catalogue  
**Category:** FAQ  
**Keywords:** service catalogue, what can I request, order, browse catalogue  
**Common items:** Software install, VPN access, new laptop, shared mailbox, peripherals, licence, data access, MFA reset, privileged access, new joiner IT bundle.  
**Agent behaviour:** When the user says browse catalogue, list these items with a one-line explanation each and offer to raise the matching RITM after confirmation.

---

# Retrieval Cheat Sheet for the Agent

| User language (examples) | Domain | Primary KB IDs (try in order) |
| --- | --- | --- |
| won't turn on / no power | Hardware | HW-001, HW-008, HW-007 |
| slow PC | Hardware | HW-002, HW-011, APP-006 |
| blue screen | Hardware | HW-003, HW-002 |
| printer | Hardware | HW-006 |
| no screen / monitor | Hardware | HW-005, HW-007 |
| camera / mic / headset | Hardware then Apps | HW-009, APP-002 |
| wifi / no internet | Network | NET-001, NET-003, NET-006 |
| VPN | Network or Access | NET-002, ACC-009, ACC-003 |
| shared drive | Network or Access | NET-005, ACC-006 |
| outlook / email | Applications | APP-001, APP-003, ACC-005 |
| teams | Applications | APP-002, HW-009, NET-003 |
| office unlicensed | Applications or Catalogue | APP-003, CAT-007 |
| locked out | Access | ACC-001, ACC-002 |
| password | Access | ACC-002 (escalate if unknown) |
| MFA | Access | ACC-003, CAT-009 |
| need software / laptop / mailbox | Catalogue | CAT-002 to CAT-008 |
| admin rights | Access | ACC-008 |

**Maximum three articles per issue.** Present one article at a time. Ask “Is this solution helpful?” after each attempt. Stop early if the user says Yes.
