<<<<<<< HEAD
local colors = require("darkpeterk.palette")

local function select_colors()
	local selected = { none = "none" }
	selected = vim.tbl_extend("force", selected, colors[vim.g.darkpeterk_config.style])
	selected = vim.tbl_extend("force", selected, vim.g.darkpeterk_config.colors)
=======
local colors = require("darkpeter.palette")

local function select_colors()
	local selected = { none = "none" }
	selected = vim.tbl_extend("force", selected, colors[vim.g.darkpeter_config.style])
	selected = vim.tbl_extend("force", selected, vim.g.darkpeter_config.colors)
>>>>>>> 68e75172a03eacfca6fee22901429e0ca2e534d6
	return selected
end

return select_colors()
