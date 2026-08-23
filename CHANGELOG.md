## v5.0.2.0 (2026-08-23)
### Login & connectivity
- New **"Test the connection"** button on the login screen: when the app can't
  reach the licence server, it now tells you exactly WHY — DNS filtering,
  firewall block on the app, antivirus HTTPS inspection, proxy — with a
  copyable report you can send us, and step-by-step fix suggestions.
- New web account page: **https://fleet.82-70-58-18.sslip.io/account** —
  create your account or test your sign-in from any browser when the app
  itself is being blocked on your PC. All "can't reach the server" messages
  now point you to both.

### Map Hack (D2 LoD files)
- The D2 runtime the installer places next to the app is now found
  automatically — fresh installs no longer get the "D2 LoD Files Not Found"
  prompt for files they already have.
- Fixed the in-app Download/Repair flow: a successful download could leave the
  app still thinking the files were missing (prompt every launch).
- Pointing the setting at a retail Diablo II install is now rejected up front
  with a clear message — a retail install never worked for map generation and
  previously failed silently.

### Server
- Licence server mirrors the game-assets download (installer fallback).

## v4.2.4 (2026-06-20)
fixed login issue for new users

## v4.2.3 (2026-06-20)


## v4.2.2 (2026-06-15)
Small edits and fixes across the board

## v4.2.2-nightly.20260612 (2026-06-12)


## v4.2.2-nightly.20260611 (2026-06-11)


## v4.2.1 (2026-06-01)
Fix chars not being visible

## v4.2.0 (2026-05-31)
Automatic character scan
Memory based char select
Char tab in accounts

Maybe more.. Yeah, more.. Some more.

## v4.1.1 (2026-05-27)
Changelog — v4.1.0

This update brings major improvements to character login, account loading, team setup, window handling, and the macro
system.

Smarter character selection

Character login has been rebuilt from the ground up.

The app now reads your character list directly from game memory as soon as each account loads, so it always knows
which characters are on each account without needing you to set anything up manually.

For accounts where a character template hasn't been built yet, the app can now use AI-powered detection (Gemini
Vision). If enabled in Settings, it sends a screenshot of the character select screen to Gemini, finds your character
automatically, and saves a template so future logins are instant. This is an optional feature that degrades gracefully
— if it fails for any reason, the existing OCR method takes over.

The quick launch slot character selector is now a dropdown, so you can pick from your known characters instead of
typing a name manually.

Teams and account setup

Setting up teams is now much easier, especially when characters don't exist yet.

When adding accounts to a team, every row now starts deselected by default, so you're never accidentally confirming
things you didn't intend to.

If an account has no characters available for a team slot, you'll now see a "Generate character" button right there in
the row. Clicking it saves a pending character with your team's Ladder/Hardcore/Expansion settings. When that account
loads next time, the character is created automatically before entering the lobby — no extra steps needed.

A new Map Characters screen makes it easier to bulk-assign character names to your whole team at once.

Window setup improvements

A few important bugs in window handling have been fixed:

Fullscreen and maximized windows are no longer knocked back to windowed mode when an account loads. The app now
detects this and skips repositioning those windows.
Your windowed resolution is no longer overwritten. Previously the app would force 1280×720 every time. Now it only
enforces that as a minimum floor — if you're running higher, that's preserved.
Frameless (borderless) mode no longer shows a white border. Three layers of suppression have been added to make sure
the border is fully gone across both Windows 10 and Windows 11.
When switching between framed and frameless mode, your client area is now preserved — the window stays the same
visible size, with the frame math handled correctly.
The window layout dialog also has new options:

A Renderless mode button that stacks windows and stops GPU rendering on idle Creator/Filler windows — saves
resources when those windows aren't doing anything
A Frameless toggle directly in the layout dialog so you can switch mode without going into Settings
Per-role resolution settings are now editable right in the dialog
Macro system — role-aware hotkeys

Macros can now be bound to specific roles.

You can assign a hotkey to only fire for Main accounts, or only for Fillers, or any other role. The hotkey listener
dispatches only to instances that match the registered role, so your team setup stays cleanly separated.

The macro builder has also been improved with better image step labels, move/offset support, and improved template
matching for custom templates including non-English filenames.

Battle.net token fetching

The account dialog now includes a "Get Token" button that fetches a Battle.net token automatically in a headless
browser session. If your account has two-factor authentication, a security code dialog will pop up asking for the code
from your email.

Activity log improvements

The activity log that gets attached to support tickets now sends the full session log as a file attachment to Discord,
making it easier to diagnose issues. Email addresses and game names/passwords are automatically scrubbed from the log
before it's sent.

Under the hood

A lot of internal work has been done to make the app more stable and reliable as team sizes grow. Character creation
during batch loading, charlist scanning, and the account loading pipeline have all been rebuilt to handle more
accounts more cleanly.

Some parts of the DPI and coordinate pipeline for multi-monitor setups are still being refined — the design work for
that is done, and the implementation will land in the next update.

## v4.1.0 (2026-05-27)
Changelog — v4.1.0

  This update brings major improvements to character login, account loading, team setup, window handling, and the macro
  system.

  ---
  Smarter character selection

  Character login has been rebuilt from the ground up.

  The app now reads your character list directly from game memory as soon as each account loads, so it always knows
  which characters are on each account without needing you to set anything up manually.

  For accounts where a character template hasn't been built yet, the app can now use AI-powered detection (Gemini
  Vision). If enabled in Settings, it sends a screenshot of the character select screen to Gemini, finds your character
  automatically, and saves a template so future logins are instant. This is an optional feature that degrades gracefully
   — if it fails for any reason, the existing OCR method takes over.

  The quick launch slot character selector is now a dropdown, so you can pick from your known characters instead of
  typing a name manually.

  ---
  Teams and account setup

  Setting up teams is now much easier, especially when characters don't exist yet.

  When adding accounts to a team, every row now starts deselected by default, so you're never accidentally confirming
  things you didn't intend to.

  If an account has no characters available for a team slot, you'll now see a "Generate character" button right there in
   the row. Clicking it saves a pending character with your team's Ladder/Hardcore/Expansion settings. When that account
   loads next time, the character is created automatically before entering the lobby — no extra steps needed.

  A new Map Characters screen makes it easier to bulk-assign character names to your whole team at once.

  ---
  Window setup improvements

  A few important bugs in window handling have been fixed:

  - Fullscreen and maximized windows are no longer knocked back to windowed mode when an account loads. The app now
  detects this and skips repositioning those windows.
  - Your windowed resolution is no longer overwritten. Previously the app would force 1280×720 every time. Now it only
  enforces that as a minimum floor — if you're running higher, that's preserved.
  - Frameless (borderless) mode no longer shows a white border. Three layers of suppression have been added to make sure
   the border is fully gone across both Windows 10 and Windows 11.
  - When switching between framed and frameless mode, your client area is now preserved — the window stays the same
  visible size, with the frame math handled correctly.

  The window layout dialog also has new options:
  - A Renderless mode button that stacks windows and stops GPU rendering on idle Creator/Filler windows — saves
  resources when those windows aren't doing anything
  - A Frameless toggle directly in the layout dialog so you can switch mode without going into Settings
  - Per-role resolution settings are now editable right in the dialog

  ---
  Macro system — role-aware hotkeys

  Macros can now be bound to specific roles.

  You can assign a hotkey to only fire for Main accounts, or only for Fillers, or any other role. The hotkey listener
  dispatches only to instances that match the registered role, so your team setup stays cleanly separated.

  The macro builder has also been improved with better image step labels, move/offset support, and improved template
  matching for custom templates including non-English filenames.

  ---
  Battle.net token fetching

  The account dialog now includes a "Get Token" button that fetches a Battle.net token automatically in a headless
  browser session. If your account has two-factor authentication, a security code dialog will pop up asking for the code
   from your email.

  ---
  Activity log improvements

  The activity log that gets attached to support tickets now sends the full session log as a file attachment to Discord,
   making it easier to diagnose issues. Email addresses and game names/passwords are automatically scrubbed from the log
   before it's sent.

  ---
  Under the hood

  A lot of internal work has been done to make the app more stable and reliable as team sizes grow. Character creation
  during batch loading, charlist scanning, and the account loading pipeline have all been rebuilt to handle more
  accounts more cleanly.

  Some parts of the DPI and coordinate pipeline for multi-monitor setups are still being refined — the design work for
  that is done, and the implementation will land in the next update.

## v4.0.1 (2026-05-21)
Changelog — Major System Update
This update brings a lot of improvements across the app, especially around window handling, onboarding, Steam loading, and setup flow.

Window setup is now much easier
A new window management system has been added.

From the overview, click Window in the pill menu to open the window setup tools. From there, you can:

Assign window positions to specific roles
Choose where each window should be placed - even pull in app!
Save your window layout
Stack windows
Spread windows across your desktop
Move windows “away” from the desktop while still keeping them active
This is still a work in progress, but it should already make setting up your layout much easier.

“Away” mode and renderless handling
You can now move windows away from the visible desktop. When doing this, you will still get a tooltip preview so you can see what is happening in the window.

The game still renders while in this mode, so it will still use some GPU and CPU.

The bigger improvement is the new renderless handling for inactive accounts. When an account is inactive, the app can reduce GPU and CPU usage and clear RAM cache. This makes the inactive game act more like a placeholder, freeing up more resources for your main game.

This can still be a little glitchy on weaker systems, especially when windows need to re-render, but for everyday use it should be very useful.

Better OCR for character login
Character name OCR has been improved.

This should make login and character detection more reliable than before.

New onboarding flow
The app now has a full new onboarding experience.

This should make it much easier for new users to understand the app and get started correctly. You can restart the onboarding anytime from Settings if you want to go through it again.

Steam loader improved
The Steam loader has been updated.

Steam can now run fully headless, while the games launch and run like normal game windows. This should make the setup cleaner, lighter, and easier to work with.

New hotkeys and quality improvements
A few new hotkeys and smaller improvements have been added across the app.

You may also notice new buttons and tools while clicking around, including a Create button.

Character and team creation
With the new ladder coming, character creation has been made easier.

You can now create characters automatically by using the new create tools. There are also improvements for batch creation of teams, making it faster to prepare full setups.

This is a big update with many changes under the hood. Some parts are still being refined, but the app should now be easier to set up, lighter to run, and smoother to use.

## v4.0.0 (2026-05-21)


## v4.0.0 (2026-05-20)
## Changelog — Major System Update

This update brings a lot of improvements across the app, especially around window handling, onboarding, Steam loading, and setup flow.

### Window setup is now much easier

A new window management system has been added.

From the overview, click **Window** in the pill menu to open the window setup tools. From there, you can:

* Assign window positions to specific roles
* Choose where each window should be placed - even pull in app!
* Save your window layout
* Stack windows
* Spread windows across your desktop
* Move windows “away” from the desktop while still keeping them active

This is still a work in progress, but it should already make setting up your layout much easier.

### “Away” mode and renderless handling

You can now move windows away from the visible desktop. When doing this, you will still get a tooltip preview so you can see what is happening in the window.

The game still renders while in this mode, so it will still use some GPU and CPU.

The bigger improvement is the new **renderless handling** for inactive accounts. When an account is inactive, the app can reduce GPU and CPU usage and clear RAM cache. This makes the inactive game act more like a placeholder, freeing up more resources for your main game.

This can still be a little glitchy on weaker systems, especially when windows need to re-render, but for everyday use it should be very useful.

### Better OCR for character login

Character name OCR has been improved.

This should make login and character detection more reliable than before.

### New onboarding flow

The app now has a full new onboarding experience.

This should make it much easier for new users to understand the app and get started correctly. You can restart the onboarding anytime from **Settings** if you want to go through it again.

### Steam loader improved

The Steam loader has been updated.

Steam can now run fully headless, while the games launch and run like normal game windows. This should make the setup cleaner, lighter, and easier to work with.

### New hotkeys and quality improvements

A few new hotkeys and smaller improvements have been added across the app.

You may also notice new buttons and tools while clicking around, including a **Create** button.

### Character and team creation

With the new ladder coming, character creation has been made easier.

You can now create characters automatically by using the new create tools. There are also improvements for batch creation of teams, making it faster to prepare full setups.

---

This is a big update with many changes under the hood. Some parts are still being refined, but the app should now be easier to set up, lighter to run, and smoother to use.

## v3.6.1-nightly.20260520 (2026-05-20)


## v3.6.1-nightly.20260520 (2026-05-20)


## v3.6.1-nightly.20260520 (2026-05-20)


## v3.6.1-nightly.20260520 (2026-05-20)


## v3.6.1-nightly.20260519 (2026-05-19)


## v3.6.0-nightly.20260505 (2026-05-05)


## v3.6.0-nightly.20260505 (2026-05-05)
Added better steam
More macros
Better team funcs
Ladder reset (chars moved to NL)
Other bits and pieces

## v3.6.0-nightly.20260504 (2026-05-04)


## v3.5.2 (2026-04-30)
Fixed some "Wrong license" issues

## v3.5.1 (2026-04-22)
increase ocr

## v3.5.0 (2026-04-21)
Steam Login support
  You can now log in D2R accounts via Steam directly from the Hub. Add your Steam username and password to an account,
  select "Steam Login" as the auth method, and launch as normal.

  Team launch with Steam accounts
  Steam accounts work in team/Quick Launch slots. Accounts are launched one at a time — each waits for the previous to
  reach character select before starting, so Steam isn't blocked by a prior session.

## v3.4.0 (2026-04-19)
Memory Manager — D2R instances are automatically trimmed when they exceed the configured RAM limit or timer interval. Long sessions stay smoother without manual intervention.

Bobarb skill keys — The Battle Command, Battle Orders, and Shout keys used during BO can now be changed in settings instead of being fixed to F1/F2/F3.

Bobarb coords — The WP and River of Flame destination clicks can be repositioned per-setup via the Edit bobarb coords panel, with a reset button to restore defaults.

Char select OCR — When an account has a character assigned, the client now scans the character select screen, finds that character by name, clicks it to select it, then clicks the lobby button. Previously it would just click lobby with whatever character happened to be highlighted.

Hotkey Fix - Added more hotkeys to your app. Now you can assign crtl + mousex2 ie.

Drop From Stash Added a simple macro to yall.

##  (2026-04-19)


## v3.2.0 (2026-04-13)
What's new

Help / Readme — rewritten
All help sections have been rewritten to reflect how the app actually works. Account setup, teams, hotkeys, quick launch, the P8 + follow automation, the license/trial flow, and the update process are all now accurate and easier to follow.

Overview — Create & Join renamed
The automation mode previously called "P8 + Follow Mode" is now split into two clearly named modes: Create Mode (your group creates and cycles games) and Join Mode (your group follows a running game sequence). The naming now matches what you're actually doing.

Trial & Payment — new flow
The upgrade and payment experience has been redesigned. Free accounts now see a Try Premium button that offers either a 3-day trial or direct purchase. Payment options (JSP, PayPal, Revolut, Crypto) open in a guided dialog that walks you through to confirmation. License activation is accessible at any point without restarting.

Main Account App — new
A separate lightweight app is now available for the player running the main character. It pairs with your filler PC and lets you trigger actions like NG and BO directly from hotkeys on your own machine — without needing the full tool open on that side. Connection status is shown at a glance and the hotkeys are fully configurable.

## v3.1.0 (2026-04-09)
Speeding up the logins!

## v3.0.0 (2026-04-08)
Freemium mode UNLOCKED!
Now you can use the loader // new game feature for FREE!
However, automation is locked to one window only!

Gamehosting menu is READY!

When you press the NG hotkey, your char will automake new game, and tell my team to move with!

Booking
Ingame management (NG, BO, Scan)
Account status
Calendar (even with press to book timeslots)
live-updated team availability
!! No End, Extend, Fillers or ingame fix buttons yet. They may come !!

## v2.0.0 (2026-04-08)
Freemium mode UNLOCKED!
Now you can use the loader // new game feature for FREE!
However, automation is locked to one window only!

Gamehosting menu is READY!

When you press the NG hotkey, your char will automake new game, and tell my team to move with!

- Booking
- Ingame management (NG, BO, Scan)
- Account status
- Calendar (even with press to book timeslots)
- live-updated team availability

!! No End, Extend, Fillers or ingame fix buttons yet. They may come !!

## v1.5.6 (2026-04-04)
Enhanced the resolution settings

## v1.5.5 (2026-04-02)
Added hotkey change for macros
Removed "Running instances" from accounts menu
Removed "Add-ons"

FEATURE REQUEST:
Change team members roles from accounts\\teams menu.  
Done sir :)

## v1.5.4 (2026-04-02)
Too many small changes....

fixed the char select again, hopefully better
fixed the lagg on login with skatesmod
added stagger to macros
probably also other stuff

## v1.5.3 (2026-03-28)
Added launch to accounts

## v1.5.1 (2026-03-28)
Runtime fix (build missed a file)

## v1.5.0 (2026-03-27)
I think I managed to get char select to work!

## v1.4.20 (2026-03-27)
- Logging in with a token is now more reliable and faster                                                               
  - The installer now shows the correct icon
  - The download link for the installer will never change going forward

## v1.4.19 (2026-03-27)
Fixing char read with token login

## v1.4.18 (2026-03-27)


## v1.4.10 (2026-03-27)


## v1.4.9 (2026-03-26)
Update stability

User Link to Key

## v1.4.8 (2026-03-26)
Another res fix

## v1.4.7 (2026-03-26)
Roll back improved.

## v1.4.6 (2026-03-26)
- New “Updates & Rollback” panel with current version and historical previous release items
- Each item shows version and notes preview
- Revert button with confirmation flow
- Downloads and validates selected version in temporary space
- Preserves settings/data and restarts app automatically on apply

## v0.0.2-nightly.20260326 (2026-03-26)
test res

## v1.4.5 (2026-03-25)


## v1.4.1 (2026-03-25)
Resolution & Window Freedom

The tool now works with D2R at any resolution and any window size — no setup needed
Play fullscreen? Main stays fullscreen the entire time, macros run without touching your screen
Play windowed? Keep whatever size you like — the tool adapts to it automatically
All macros (rush, create game, join, BO barb, etc.) now scale to your screen perfectly

Creator Role

A new built-in role that takes over game creation from Main. When a Creator is on the team, it creates the game while   Main joins alongside the rest of the team. Without a Creator, everything works exactly as before — Main creates as
usual.

## v1.0.26 (2026-03-25)
Introducing themes Check your settings.

