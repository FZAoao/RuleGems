package org.cubexmc.gui;

import org.bukkit.Material;
import org.bukkit.inventory.ItemStack;
import org.cubexmc.manager.GemManager;
import org.cubexmc.manager.LanguageManager;

/**
 * 主菜单 GUI - 提供导航到宝石列表和统治者列表
 * 
 * 布局 (27格 3x9):
 * ┌─────────────────────────────────────────┐
 * │ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ ▬ │ 装饰行
 * │ ▬ 💎 👤 💠 👑 🏛 🧭 ▬ │ 功能行
 * │ ▬ ▬ ▬ ▬ ✕ ▬ ▬ ▬ ▬ │ 控制行
 * └─────────────────────────────────────────┘
 */
public class MainMenuGUI extends ChestMenu {

    private static final int GUI_SIZE = 27;
    private static final int SLOT_GEMS = 10;
    private static final int SLOT_PROFILE = 11;
    private static final int SLOT_REDEEM = 12;
    private static final int SLOT_RULERS = 14;
    private static final int SLOT_CABINET = 15;
    private static final int SLOT_NAVIGATE = 16;
    private static final int SLOT_CLOSE = 22;

    private final GemManager gemManager;
    private final LanguageManager lang;

    public MainMenuGUI(GUIManager guiManager, GemManager gemManager, LanguageManager languageManager) {
        super(guiManager);
        this.gemManager = gemManager;
        this.lang = languageManager;
    }

    private String msg(String path) {
        return org.bukkit.ChatColor.translateAlternateColorCodes('&', lang.getMessage("gui." + path));
    }

    private String rawMsg(String path) {
        return lang.getMessage("gui." + path);
    }

    // ------------------------------------------------------------------
    // ChestMenu contract
    // ------------------------------------------------------------------

    @Override
    protected String getTitle() {
        return msg("menu.title");
    }

    @Override
    protected int getSize() {
        return GUI_SIZE;
    }

    @Override
    protected GUIHolder.GUIType getHolderType() {
        return GUIHolder.GUIType.MAIN_MENU;
    }

    @Override
    protected void populate(org.bukkit.inventory.Inventory gui, GUIHolder holder) {
        // 填充背景
        ItemStack filler = ItemBuilder.filler();
        for (int i = 0; i < GUI_SIZE; i++)
            gui.setItem(i, filler);

        gui.setItem(SLOT_GEMS, createGemsButton(gemManager.getAllGemUuids().size(), holder.isAdmin()));
        gui.setItem(SLOT_PROFILE, createProfileButton());
        gui.setItem(SLOT_REDEEM, createRedeemGuideButton());
        gui.setItem(SLOT_RULERS, createRulersButton(gemManager.getCurrentRulers().size(), holder.isAdmin()));
        gui.setItem(SLOT_CABINET, createCabinetButton(holder));
        gui.setItem(SLOT_NAVIGATE, createNavigateButton());
        gui.setItem(SLOT_CLOSE, ItemBuilder.closeButton(manager.getNavActionKey(), rawMsg("control.close")));
    }

    // No item-click handling needed — navigation items handle everything.

    /**
     * 创建宝石按钮
     */
    private ItemStack createGemsButton(int gemCount, boolean isAdmin) {
        Material material = Material.DIAMOND;

        ItemBuilder builder = new ItemBuilder(material)
                .name("&b" + rawMsg("menu.gems_title"))
                .data(manager.getNavActionKey(), "open_gems")
                .glow();

        builder.addEmptyLore()
                .addLore("&7" + rawMsg("menu.gems_desc"))
                .addEmptyLore()
                .addLore("&e▸ " + rawMsg("menu.gem_count") + ": &f" + gemCount);

        if (isAdmin) {
            builder.addEmptyLore()
                    .addLore("&8" + rawMsg("menu.admin_view"));
        }

        builder.addEmptyLore()
                .addLore("&a» " + rawMsg("menu.click_to_open"));

        return builder.build();
    }

    /**
     * 创建统治者按钮
     */
    private ItemStack createRulersButton(int rulerCount, boolean isAdmin) {
        Material material = Material.GOLDEN_HELMET;

        ItemBuilder builder = new ItemBuilder(material)
                .name("&6" + rawMsg("menu.rulers_title"))
                .data(manager.getNavActionKey(), "open_rulers")
                .hideAttributes()
                .glow();

        builder.addEmptyLore()
                .addLore("&7" + rawMsg("menu.rulers_desc"))
                .addEmptyLore()
                .addLore("&e▸ " + rawMsg("menu.ruler_count") + ": &f" + rulerCount);

        if (isAdmin) {
            builder.addEmptyLore()
                    .addLore("&8" + rawMsg("menu.admin_view"));
        }

        builder.addEmptyLore()
                .addLore("&a» " + rawMsg("menu.click_to_open"));

        return builder.build();
    }

    private ItemStack createRedeemGuideButton() {
        boolean redeemEnabled = manager.getPlugin().getGameplayConfig().isRedeemEnabled();
        boolean redeemAllEnabled = manager.getPlugin().getGameplayConfig().isFullSetGrantsAllEnabled();
        boolean holdEnabled = manager.getPlugin().getGameplayConfig().isHoldToRedeemEnabled();
        boolean placeEnabled = manager.getPlugin().getGameplayConfig().isPlaceRedeemEnabled();
        boolean sneakToRedeem = manager.getPlugin().getGameplayConfig().isSneakToRedeem();

        ItemBuilder builder = new ItemBuilder(Material.EMERALD)
                .name("&a" + rawMsg("menu.redeem_title"))
                .data(manager.getNavActionKey(), "show_redeem_help")
                .glow();

        builder.addEmptyLore()
                .addLore("&7" + rawMsg("menu.redeem_desc"))
                .addEmptyLore();

        if (redeemEnabled) {
            builder.addLore("&e▸ " + rawMsg("menu.redeem_command"));
        } else {
            builder.addLore("&c▸ " + rawMsg("menu.redeem_disabled"));
        }

        if (holdEnabled) {
            builder.addLore("&e▸ " + rawMsg(sneakToRedeem ? "menu.redeem_hold_sneak" : "menu.redeem_hold_normal"));
        }

        if (placeEnabled) {
            builder.addLore("&e▸ " + rawMsg("menu.redeem_altar"));
        }

        if (redeemAllEnabled) {
            builder.addLore("&e▸ " + rawMsg("menu.redeem_all"));
        }

        builder.addEmptyLore()
                .addLore("&8" + rawMsg("menu.info_only"));
        return builder.build();
    }

    private ItemStack createProfileButton() {
        return new ItemBuilder(Material.BOOK)
                .name("&b" + rawMsg("menu.profile_title"))
                .addEmptyLore()
                .addLore("&7" + rawMsg("menu.profile_desc"))
                .addEmptyLore()
                .addLore("&a» " + rawMsg("menu.click_to_open"))
                .data(manager.getNavActionKey(), "open_profile")
                .hideAttributes()
                .build();
    }

    private ItemStack createCabinetButton(GUIHolder holder) {
        boolean appointEnabled = manager.getPlugin().getFeatureManager() != null
                && manager.getPlugin().getFeatureManager().getAppointFeature() != null
                && manager.getPlugin().getFeatureManager().getAppointFeature().isEnabled();
        org.bukkit.entity.Player viewer = manager.getPlugin().getServer().getPlayer(holder.getViewerId());
        boolean canManageAppointments = appointEnabled && holder.isAdmin();
        if (!canManageAppointments && appointEnabled && viewer != null && manager.getPlugin().getFeatureManager() != null
                && manager.getPlugin().getFeatureManager().getAppointFeature() != null) {
            canManageAppointments = manager.getPlugin().getFeatureManager().getAppointFeature()
                    .getAppointDefinitions().keySet().stream()
                    .anyMatch(key -> viewer.hasPermission("rulegems.appoint." + key)
                            || viewer.hasPermission("rulegems.appoint."
                                    + key.toLowerCase(java.util.Locale.ROOT)));
        }

        ItemBuilder builder = new ItemBuilder(Material.WRITABLE_BOOK)
                .name("&d" + rawMsg("menu.cabinet_title"))
                .addEmptyLore()
                .addLore("&7" + rawMsg("menu.cabinet_desc"))
                .addEmptyLore();

        if (canManageAppointments) {
            builder.addLore("&a» " + rawMsg("menu.click_to_open"))
                    .data(manager.getNavActionKey(), "open_cabinet")
                    .glow();
        } else {
            builder.addLore("&8" + rawMsg("menu.info_only"))
                    .addLore("&7" + rawMsg("menu.cabinet_unavailable"))
                    .hideAttributes();
        }
        return builder.build();
    }

    private ItemStack createNavigateButton() {
        boolean navigateEnabled = manager.getPlugin().getFeatureManager() != null
                && manager.getPlugin().getFeatureManager().getNavigator() != null
                && manager.getPlugin().getFeatureManager().getNavigator().isEnabled();

        ItemBuilder builder = new ItemBuilder(Material.COMPASS)
                .name("&e" + rawMsg("menu.navigate_title"))
                .data(manager.getNavActionKey(), "show_navigate_help")
                .hideAttributes();

        builder.addEmptyLore()
                .addLore("&7" + rawMsg("menu.navigate_desc"))
                .addEmptyLore();

        if (navigateEnabled) {
            builder.addLore("&e▸ " + rawMsg("menu.navigate_hint"));
            builder.addLore("&e▸ " + rawMsg("menu.navigate_permission"));
        } else {
            builder.addLore("&c▸ " + rawMsg("menu.navigate_disabled"));
        }

        builder.addEmptyLore()
                .addLore("&8" + rawMsg("menu.info_only"));
        return builder.build();
    }
}
