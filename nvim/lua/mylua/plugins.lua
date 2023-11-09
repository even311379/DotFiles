local fn = vim.fn

-- Automatically install packer
local install_path = fn.stdpath "data" .. "/site/pack/packer/start/packer.nvim"
if fn.empty(fn.glob(install_path)) > 0 then
    PACKER_BOOTSTRAP = fn.system {
        "git",
        "clone",
        "--depth",
        "1",
        "https://github.com/wbthomason/packer.nvim",
        install_path,
    }
    print "Installing packer close and reopen neovim..."
    vim.cmd [[packadd packer.nvim]]
end


-- Autocommand that reloads neovim whenever you save the plugins.lua file
vim.cmd [[
    augroup packer_user_config
        autocmd!
        autocmd BufWritePost plugins.lua source <afile> | PackerSync
    augroup end
]]

-- Use a protected call so we don't error out on first use
local status_ok, packer = pcall(require, "packer")
if not status_ok then
    return
end

-- Have packer use a popupo window
packer.init {
    display = {
        open_fn = function()
            return require("packer.util").float { border = "rounded"}
        end,
    },
}

-- Install my plugins here
return packer.startup(function(use)

    use "wbthomason/packer.nvim" -- packer itself
    -- tons of plugins rely on the next two plugins
    use "nvim-lua/popup.nvim"  -- popup api from neovim
    use "nvim-lua/plenary.nvim" -- useful functions for lots of plugins?
    use "numToStr/Comment.nvim" -- Easily comment stuff
    use "nvim-tree/nvim-web-devicons"
    use "nvim-tree/nvim-tree.lua" -- nvim tree
    use "stevearc/oil.nvim"  -- oil
    use "akinsho/bufferline.nvim"
    use "moll/vim-bbye"
    use "nvim-lualine/lualine.nvim" -- better status line?
    use {
        "lukas-reineke/indent-blankline.nvim",
        main="ibl"
    }
    use "akinsho/toggleterm.nvim"
    use "ahmedkhalf/project.nvim"


    -- cmp plugins
    use "hrsh7th/nvim-cmp"
    use "hrsh7th/cmp-buffer"
    use "hrsh7th/cmp-path"
    use "hrsh7th/cmp-cmdline"
    use "saadparwaiz1/cmp_luasnip" -- snip?
    use "hrsh7th/cmp-nvim-lsp"

    -- snippets
    use "L3MON4D3/LuaSnip" -- lua snip engine
    use "rafamadriz/friendly-snippets" -- helper snips?

    -- LSP
    use "neovim/nvim-lspconfig"
    use "williamboman/mason.nvim"
    use "williamboman/mason-lspconfig.nvim"
    use 'jose-elias-alvarez/null-ls.nvim'
    
    -- color schemes
    use "lunarvim/colorschemes"
    use "folke/tokyonight.nvim"
    use "cocopon/iceberg.vim"
    use "morhetz/gruvbox"

    use "xiyaowong/transparent.nvim" -- transparent

    -- Telescope
    use "nvim-telescope/telescope.nvim"
    use "nvim-telescope/telescope-media-files.nvim"

    -- Tree sitter
    use "nvim-treesitter/nvim-treesitter"
    use "hiphish/rainbow-delimiters.nvim"
    use "JoosepAlviste/nvim-ts-context-commentstring"


    -- others
    use "windwp/nvim-autopairs"
    use "goolord/alpha-nvim"
    use "folke/which-key.nvim"

    if PACKER_BOOTSTRAP then
        require("packer").sync()
    end
end)



--[[
--here is all the options packer plugin provided:
use {
  'myusername/example',        -- The plugin location string
  -- The following keys are all optional
  disable = boolean,           -- Mark a plugin as inactive
  as = string,                 -- Specifies an alias under which to install the plugin
  installer = function,        -- Specifies custom installer. See "custom installers" below.
  updater = function,          -- Specifies custom updater. See "custom installers" below.
  after = string or list,      -- Specifies plugins to load before this plugin. See "sequencing" below
  rtp = string,                -- Specifies a subdirectory of the plugin to add to runtimepath.
  opt = boolean,               -- Manually marks a plugin as optional.
  bufread = boolean,           -- Manually specifying if a plugin needs BufRead after being loaded
  branch = string,             -- Specifies a git branch to use
  tag = string,                -- Specifies a git tag to use. Supports '*' for "latest tag"
  commit = string,             -- Specifies a git commit to use
  lock = boolean,              -- Skip updating this plugin in updates/syncs. Still cleans.
  run = string, function, or table, -- Post-update/install hook. See "update/install hooks".
  requires = string or list,   -- Specifies plugin dependencies. See "dependencies".
  rocks = string or list,      -- Specifies Luarocks dependencies for the plugin
  config = string or function, -- Specifies code to run after this plugin is loaded.
  -- The setup key implies opt = true
  setup = string or function,  -- Specifies code to run before this plugin is loaded. The code is ran even if
                               -- the plugin is waiting for other conditions (ft, cond...) to be met.
  -- The following keys all imply lazy-loading and imply opt = true
  cmd = string or list,        -- Specifies commands which load this plugin. Can be an autocmd pattern.
  ft = string or list,         -- Specifies filetypes which load this plugin.
  keys = string or list,       -- Specifies maps which load this plugin. See "Keybindings".
  event = string or list,      -- Specifies autocommand events which load this plugin.
  fn = string or list          -- Specifies functions which load this plugin.
  cond = string, function, or list of strings/functions,   -- Specifies a conditional test to load this plugin
  module = string or list      -- Specifies Lua module names for require. When requiring a string which starts
                               -- with one of these module names, the plugin will be loaded.
  module_pattern = string/list -- Specifies Lua pattern of Lua module names for require. When
                               -- requiring a string which matches one of these patterns, the plugin will be loaded.
}
]]--

