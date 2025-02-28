for k in pairs(package.loaded) do
    if k:match(".*darkpeter.*") then package.loaded[k] = nil end
end

require('darkpeter').setup()
require('darkpeter').colorscheme()
