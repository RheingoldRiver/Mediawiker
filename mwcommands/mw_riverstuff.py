DEFAULT_NEW_CLASS_TEXT = """local Class = require('Module:Class').Class
local MarkupObject = require('Module:MarkupObjectClass')

local p = Class(MarkupObject)

function p:new(str)
	self:super(str, 'REPLACE')
	if self.unknown then
		error('Unrecognized REPLACE name: ' .. tostring(str))
	end
end

return p"""

DEFAULT_NEW_MODULE_TEXT = """local util_args = require('Module:ArgsUtil')
local util_cargo = require("Module:CargoUtil")
local util_html = require("Module:HtmlUtil")
local util_map = require('Module:MapUtil')
local util_table = require("Module:TableUtil")
local util_text = require("Module:TextUtil")
local util_vars = require("Module:VarsUtil")
local i18n = require("Module:I18nUtil")
local lang = mw.getLanguage('en')

local h = {{}}

local p = {{}}
function p.main(frame)
	local args = util_args.merge(true)
	i18n.init('{}')
end
return p"""


def get_new_text(page_name, namespace):
	if namespace == 828:
		title_without_namespace = page_name.replace('Module:', '')
		if page_name.lower().endswith('/doc'):
			return '<includeonly>{{luadoc}}[[Category:Lua Modules]]</includeonly>'
		elif page_name.lower().endswith('/i18n'):
			return 'return {\n\t["en"] = {\n\t\t\n\t}\n}'
		elif page_name.endswith('Class'):
			return DEFAULT_NEW_CLASS_TEXT
		else:
			return DEFAULT_NEW_MODULE_TEXT.format(title_without_namespace)
	elif page_name.lower().endswith('.js'):
		return "$( function () {\n		if (! document.getElementById('')) {\nreturn;\n});"
	else:
		return '<!-- New wiki page: Remove this with text of the new page -->'
