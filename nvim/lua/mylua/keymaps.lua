local opts = { noremap = true, silent = false }

local term_opts = { silent = false }

local keymap = vim.api.nvim_set_keymap

keymap("", "<Space>", "<Nop>", opts)
vim.g.mapleader = " "
vim.g.maplocallearder = " "

-- Modes
-- normal = n
-- insert = i
-- visual = v
-- visual block = x
-- term = t
-- command = c

-- Normal --
-- Better split window navigation
keymap("n", "<C-h>", "<C-w>h", opts)
keymap("n", "<C-j>", "<C-w>j", opts)
keymap("n", "<C-k>", "<C-w>k", opts)
keymap("n", "<C-l>", "<C-w>l", opts)

keymap("n", "<leader>e", "<cmd>NvimTreeToggle<CR>", opts) -- open nvim tree
-- <CR> is the return key in terminal mode... and it seemed <CR> == <cr> the case is totally ignored...

-- Resize split
keymap("n", "<C-Up>", ":resize +2<CR>", opts)
keymap("n", "<C-Down>", ":resize -2<CR>", opts)
keymap("n", "<C-Left>", ":vertical resize +2<CR>", opts)
keymap("n", "<C-Right>", ":vertical resize -2<CR>", opts)

-- Navigate buffers
keymap("n", "<S-l>", ":bnext<CR>", opts)
keymap("n", "<S-h>", ":bprevious<CR>", opts)

-- Move Current line up and down
-- TODO: make this work in Visual mode which can move all selected blocks...
keymap("n", "<A-Up>", ":m .-2<CR> ==", opts)
keymap("n", "<A-Down>", ":m .+1<CR> ==", opts)

-- Telescope
keymap("n", "<leader>f", "<cmd>Telescope find_files<cr>", opts)
keymap("n", "<leader>g", "<cmd>Telescope live_grep<cr>", opts)
keymap("n", "<leader>b", "<cmd>Telescope buffers<cr>", opts)

-- Comment ... make it more common binding?
keymap("n", "<C-_>", "gcc", {}) -- so weird... control + / need this bindings?
keymap("n", ",c", "gcc", {}) -- add opts will make these binding fail...

keymap("n", "<C-\\>", "<cmd>ToggleTerm<CR>", opts) -- add opts will make these binding fail...


-- Insert--
-- fast exit insert?
keymap("i", "jk", "<ESC>", opts)

-- move current line
keymap("i", "<A-Up>", "<ESC>:m .-2<CR>==gi", opts)
keymap("i", "<A-Down>", "<ESC>:m .+1<CR>==gi", opts)

-- Comment ... make it more common binding?
keymap("i", "<C-_>", "<ESC>gcc<CR>==gi", {}) -- so weird... control + / need this bindings?

-- Visual --
-- stay in indent mode
keymap("v", "<", "<gv", opts)
keymap("v", ">", ">gv", opts)

-- move current line
-- keymap("v", "<A-Up>", ":m .-2<CR>gv==gv", opts)
-- keymap("v", "<A-Down>", ":m .+1<CR>gv==gv", opts)
keymap("v", "<A-Down>", ":m .+1<CR>==", opts)
keymap("v", "<A-Up>", ":m .-2<CR>==", opts)

-- Make paste so much make sense
keymap("v", "p", '"_dP', opts)

-- Comment ... make it more common binding?
keymap("v", "<C-_>", "gcc", {}) -- so weird... control + / need this bindings?

-- Visual Block
-- Move text up and down
keymap("x", "<A-Down>", ":move '>+1<CR>gv-gv", opts)
keymap("x", "<A-Up>", ":move '<-2<CR>gv-gv", opts)


