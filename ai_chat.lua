local Tinkr = ...
local FrameEvent = Tinkr.Util.FrameEvent

local delay = 20
local last_reply = ''
local player_waiting = ''
local input_file = 'message.txt'
local output_file = 'response.txt'
local waiting_for_response = false

local process_whisper = function(...)
    if waiting_for_response then return end
    local message, player_name = ...
    local success = WriteFile(input_file, message, false)
    if success then
        Tinkr:log("Message written to AI: " .. message)
        waiting_for_response = true
        player_waiting = player_name
    end
end

FrameEvent:Register('CHAT_MSG_WHISPER', process_whisper)

local process_response = function()
    if not waiting_for_response then return end
    local message = ReadFile(output_file)
    if message == last_reply then return end
    if message then
        Tinkr:log("Response read from AI: " .. message)
        waiting_for_response = false
        last_reply = message
        SendChatMessage(message, "WHISPER", nil, player_waiting);
    end
end

C_Timer.NewTicker(delay, process_response)