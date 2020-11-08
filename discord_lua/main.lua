local discordia = require('discordia')
local math = require('math')
local config = require('config')
local os = require('os')

local wait = function(seconds)
    local start = os.time()
    repeat until os.time() > start + seconds
  end

local choice = function(x)
    return x[math.random(1, table.getn(x))]
end

local bot = discordia.Client()
local prefix = "$"

local activity = {}
activity['name'] = config.activ_name
activity['type'] = 2

bot:on('ready', function()
	print('Logged in as '.. bot.user.username)
end)

bot:on('messageCreate', function(message)
    if message.content == tostring(string.format("%sping ShGbot", prefix)) then
        message:delete()
		message.channel:send('Lua ready to fisting ass')
	end
end)

bot:on('messageCreate', function(message)
    if message.content == tostring(string.format("%sgogi_noob", prefix)) then
        message.channel:send("Gog anus")
        end
    end)

bot:run('Bot ' .. tostring(config.TOKEN))
bot:setGame(activity)
bot:setStatus(config.status_type)
