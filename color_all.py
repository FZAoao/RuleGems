import re

file_path = "c:/Users/Angus/Desktop/RuleGems/lang.yml"

replacements = {
    # control
    r"prev: Previous": r"prev: '&#FFE066Previous'",
    r"next: Next": r"next: '&#FFE066Next'",
    r"page: Page": r"page: '&#CFD8DCPage'",
    r"total: Total": r"total: '&#CFD8DCTotal'",
    r"close: Close": r"close: '&#E63946Close'",
    r"back: Back": r"back: '&#F4D03FBack'",
    r"refresh: Refresh": r"refresh: '&#69DB7CRefresh'",
    r"filter: Filter": r"filter: '&#FFE066Filter'",
    r"filter_hint: Click to toggle filter": r"filter_hint: '&#CFD8DCClick to toggle filter'",
    
    # gems
    r"filter_all: All": r"filter_all: '&#F1F5F9All'",
    
    # rulers
    r"no_rulers: No Rulers": r"no_rulers: '&#E63946No Rulers'",
    r"no_rulers_lore: No players have redeemed gems": r"no_rulers_lore: '&#CFD8DCNo players have redeemed gems'",
    r"supreme_ruler: Supreme Ruler": r"supreme_ruler: '&#F4D03FSupreme Ruler'",
    r"supreme_ruler_desc: Collected all gems!": r"supreme_ruler_desc: '&#CFD8DCCollected all gems!'",
    r"holding_gems: Holding Gems": r"holding_gems: '&#FFE066Holding Gems'",
    r"status_online: Online": r"status_online: '&#69DB7COnline'",
    r"status_offline: Offline": r"status_offline: '&#CFD8DCOffline'",
    r"click_tp_player: Click to teleport to player": r"click_tp_player: '&#FFE066Click to teleport to player'",
    r"click_view_appointees: Click to view appointees": r"click_view_appointees: '&#FFE066Click to view appointees'",
    r"shift_click_tp: Shift\+Click to teleport": r"shift_click_tp: '&#FFE066Shift+Click to teleport'",
    
    # appointees
    r"no_appointees: No Appointees": r"no_appointees: '&#E63946No Appointees'",
    r"no_appointees_lore: This ruler has not appointed anyone": r"no_appointees_lore: '&#CFD8DCThis ruler has not appointed anyone'",
    r"position: 'Position:'": r"position: '&#FFE066Position:'",
    r"permissions: Permissions": r"permissions: '&#FFE066Permissions'",
    r"allowed_commands: Allowed Commands": r"allowed_commands: '&#FFE066Allowed Commands'",
    r"delegate_permissions: Delegate Permissions": r"delegate_permissions: '&#FFE066Delegate Permissions'",
    r"conditions: Conditions": r"conditions: '&#FFE066Conditions'",
    r"condition_time_always: Always": r"condition_time_always: '&#F1F5F9Always'",
    r"can_appoint: Can appoint": r"can_appoint: '&#FFE066Can appoint'",
    r"click_tp: Click to teleport": r"click_tp: '&#FFE066Click to teleport'",
    r"shift_click_dismiss: Shift\+Click to dismiss": r"shift_click_dismiss: '&#E63946Shift+Click to dismiss'",
    
    # menu
    r"gems_title: Gems List": r"gems_title: '&#FFE066Gems List'",
    r"gems_desc: View all power gems status": r"gems_desc: '&#CFD8DCView all power gems status'",
    r"rulers_title: Rulers List": r"rulers_title: '&#FFE066Rulers List'",
    r"rulers_desc: View current power holders": r"rulers_desc: '&#CFD8DCView current power holders'",
    r"gem_count: Gem Count": r"gem_count: '&#FFE066Gem Count'",
    r"ruler_count: Ruler Count": r"ruler_count: '&#FFE066Ruler Count'",
    r"admin_view: Admin View": r"admin_view: '&#E63946Admin View'",
    r"click_to_open: Click to open": r"click_to_open: '&#FFE066Click to open'",
    r"profile_title: My Powers": r"profile_title: '&#FFE066My Powers'",
    r"profile_desc: Review your current rule powers, appointments, and commands": r"profile_desc: '&#CFD8DCReview your current rule powers, appointments, and commands'",
    r"redeem_title: Redeem Guide": r"redeem_title: '&#FFE066Redeem Guide'",
    r"redeem_desc: Learn the fastest ways to turn gems into power": r"redeem_desc: '&#CFD8DCLearn the fastest ways to turn gems into power'",
    r"redeem_command: Use /rg redeem with a gem in your main hand": r"redeem_command: '&#CFD8DCUse /rg redeem with a gem in your main hand'",
    r"redeem_disabled: Manual redeem is currently disabled": r"redeem_disabled: '&#E63946Manual redeem is currently disabled'",
    r"redeem_hold_sneak: Sneak \+ hold right-click to redeem": r"redeem_hold_sneak: '&#CFD8DCSneak + hold right-click to redeem'",
    r"redeem_hold_normal: Hold right-click to redeem": r"redeem_hold_normal: '&#CFD8DCHold right-click to redeem'",
    r"redeem_altar: Some gems can be redeemed at their altar": r"redeem_altar: '&#CFD8DCSome gems can be redeemed at their altar'",
    r"redeem_all: Use /rg redeemall after collecting the full set": r"redeem_all: '&#CFD8DCUse /rg redeemall after collecting the full set'",
    r"cabinet_title: Cabinet": r"cabinet_title: '&#F48FB1Cabinet'",
    r"cabinet_desc: Manage appointable roles and handle staffing in one place": r"cabinet_desc: '&#CFD8DCManage appointable roles and handle staffing in one place'",
    r"cabinet_unavailable: You do not currently control any appointable roles": r"cabinet_unavailable: '&#E63946You do not currently control any appointable roles'",
    r"navigate_title: Compass Navigation": r"navigate_title: '&#CDE0F5Compass Navigation'",
    r"navigate_desc: Track placed gems and learn the exploration loop": r"navigate_desc: '&#CFD8DCTrack placed gems and learn the exploration loop'",
    r"navigate_hint: Right-click a compass to point at the nearest gem": r"navigate_hint: '&#FFE066Right-click a compass to point at the nearest gem'",
    r"navigate_permission: Requires the rulegems\.navigate permission": r"navigate_permission: '&#E63946Requires the rulegems.navigate permission'",
    r"navigate_disabled: Compass navigation is currently disabled": r"navigate_disabled: '&#E63946Compass navigation is currently disabled'",
    r"info_only: Info only": r"info_only: '&#CFD8DCInfo only'",
    r"no_more_info: No more info": r"no_more_info: '&#CFD8DCNo more info'",
    
    # profile
    r"identity_title: Identity": r"identity_title: '&#FFE066Identity'",
    r"player_name: Player": r"player_name: '&#CDE0F5Player'",
    r"player_uuid: UUID": r"player_uuid: '&#CFD8DCUUID'",
    r"ruler_title: Ruler Powers": r"ruler_title: '&#F4D03FRuler Powers'",
    r"ruler_none: You have not redeemed any ruling gems": r"ruler_none: '&#CFD8DCYou have not redeemed any ruling gems'",
    r"ruler_full_set: You currently own the full set": r"ruler_full_set: '&#69DB7CYou currently own the full set'",
    r"appointments_title: Granted Roles": r"appointments_title: '&#FFE066Granted Roles'",
    r"appointments_none: You do not currently hold any appointed roles": r"appointments_none: '&#CFD8DCYou do not currently hold any appointed roles'",
    r"system: System": r"system: '&#82B1FFSystem'",
    r"commands_title: Allowed Commands": r"commands_title: '&#FFE066Allowed Commands'",
    r"command_count: Command Count": r"command_count: '&#FFE066Command Count'",
    r"commands_summary: The list below shows your current command allowances and cooldowns": r"commands_summary: '&#CFD8DCThe list below shows your current command allowances and cooldowns'",
    r"no_commands: No commands available": r"no_commands: '&#CFD8DCNo commands available'",
    r"no_commands_lore: This fills automatically when your current powers grant command\n\s*allowances": r"no_commands_lore: '&#CFD8DCThis fills automatically when your current powers grant command\n      allowances'",
    r"remaining_uses: Remaining Uses": r"remaining_uses: '&#FFE066Remaining Uses'",
    r"cooldown: Cooldown": r"cooldown: '&#FFE066Cooldown'",
    r"cooldown_ready: Ready": r"cooldown_ready: '&#69DB7CReady'",
    r"manage_powers_title: ⚙ Manage Gem Powers": r"manage_powers_title: '&#FFE066⚙ Manage Gem Powers'",
    r"manage_powers_lore: Click to open the panel to toggle your gem powers on or off": r"manage_powers_lore: '&#CFD8DCClick to open the panel to toggle your gem powers on or off'",
    
    # cabinet
    r"no_roles: No roles available": r"no_roles: '&#E63946No roles available'",
    r"no_roles_lore: Appointable roles appear here once one of your powers grants them": r"no_roles_lore: '&#CFD8DCAppointable roles appear here once one of your powers grants them'",
    r"current_count: Filled Slots": r"current_count: '&#FFE066Filled Slots'",
    r"current_members: Current Members": r"current_members: '&#CDE0F5Current Members'",
    r"none: None yet": r"none: '&#CFD8DCNone yet'",
    r"click_manage: Click to manage this role": r"click_manage: '&#FFE066Click to manage this role'",
    
    # cabinet members
    r"no_candidates: Nothing to manage": r"no_candidates: '&#CFD8DCNothing to manage'",
    r"no_candidates_lore: No eligible online targets and no current appointees were\n\s*found": r"no_candidates_lore: '&#CFD8DCNo eligible online targets and no current appointees were\n      found'",
    r"status: Status": r"status: '&#FFE066Status'",
    r"status_appointed: Currently appointed by you": r"status_appointed: '&#69DB7CCurrently appointed by you'",
    r"status_available: Ready to appoint": r"status_available: '&#FFE066Ready to appoint'",
    r"appoint_hint: Click to appoint this player": r"appoint_hint: '&#FFE066Click to appoint this player'",
    r"dismiss_hint: Click to dismiss this player": r"dismiss_hint: '&#E63946Click to dismiss this player'",
    
    # toggles
    r"back_to_profile: Back to Profile": r"back_to_profile: '&#FFE066Back to Profile'",
    r"no_gems: No gems available": r"no_gems: '&#E63946No gems available'",
    r"no_gems_lore: You do not currently own any gems": r"no_gems_lore: '&#CFD8DCYou do not currently own any gems'",
    r"status_off: 'Current status: Disabled'": r"status_off: '&#CFD8DCCurrent status: &#E63946Disabled'",
    r"click_to_enable: Click to enable this gem's power": r"click_to_enable: '&#69DB7CClick to enable this gem\'s power'",
    r"status_on: 'Current status: Enabled'": r"status_on: '&#CFD8DCCurrent status: &#69DB7CEnabled'",
    r"click_to_disable: Click to disable this gem's power \(disables your effects and\n\s*commands, does not affect appointees\)": r"click_to_disable: '&#E63946Click to disable this gem\'s power (disables your effects and\n      commands, does not affect appointees)'",
    
    # condition
    r"time_day: Day only": r"time_day: '&#FFE066Day only'",
    r"time_night: Night only": r"time_night: '&#3B5BDBNight only'",
    r"time_custom: Time": r"time_custom: '&#CFD8DCTime'",
    r"world_whitelist: 'Only in: '": r"world_whitelist: '&#69DB7COnly in: '",
    r"world_blacklist: 'Except: '": r"world_blacklist: '&#E63946Except: '",
    r"no_limit: No restrictions": r"no_limit: '&#69DB7CNo restrictions'",
    
    # player
    r"unknown_offline: Unknown \(offline\)": r"unknown_offline: '&#CFD8DCUnknown (offline)'",
}

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

for pattern_str, repl in replacements.items():
    content = re.sub(pattern_str, repl, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Uncolored keys updated successfully.")
