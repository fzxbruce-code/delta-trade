/**
 * Delta Trade - 主题管理系统
 * 支持浅色/深色/系统自动主题切换
 */

class ThemeManager {
  constructor() {
    this.storageKey = 'delta-trade-theme';
    this.init();
  }

  init() {
    // 应用保存的主题或系统主题
    const savedTheme = this.getSavedTheme();
    this.applyTheme(savedTheme);
    
    // 监听系统主题变化
    this.watchSystemTheme();
    
    // 初始化切换按钮
    this.initToggle();
  }

  getSavedTheme() {
    return localStorage.getItem(this.storageKey) || 'system';
  }

  getSystemTheme() {
    return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
  }

  applyTheme(theme) {
    const root = document.documentElement;
    
    if (theme === 'system') {
      root.removeAttribute('data-theme');
      localStorage.setItem(this.storageKey, 'system');
    } else {
      root.setAttribute('data-theme', theme);
      localStorage.setItem(this.storageKey, theme);
    }
    
    this.updateToggleUI(theme);
  }

  watchSystemTheme() {
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => {
      if (this.getSavedTheme() === 'system') {
        // 如果是系统模式，重新应用以触发更新
        this.applyTheme('system');
      }
    });
  }

  initToggle() {
    document.addEventListener('click', (e) => {
      const option = e.target.closest('.theme-toggle-option');
      if (option && option.dataset.theme) {
        this.applyTheme(option.dataset.theme);
      }
    });
  }

  updateToggleUI(activeTheme) {
    const options = document.querySelectorAll('.theme-toggle-option');
    options.forEach(option => {
      const isActive = option.dataset.theme === activeTheme;
      option.classList.toggle('active', isActive);
      option.setAttribute('aria-checked', isActive);
    });
  }
}

// 初始化主题管理器
document.addEventListener('DOMContentLoaded', () => {
  window.themeManager = new ThemeManager();
});

// 立即应用主题（避免闪烁）
(function() {
  const savedTheme = localStorage.getItem('delta-trade-theme');
  if (savedTheme && savedTheme !== 'system') {
    document.documentElement.setAttribute('data-theme', savedTheme);
  }
})();
