# -*- encoding: utf-8 -*-
'''
     ██╗██╗   ██╗██╗   ██╗███╗   ██╗██╗  ██╗ ██████╗ 
     ██║╚██╗ ██╔╝██║   ██║████╗  ██║██║ ██╔╝██╔═══██╗
     ██║ ╚████╔╝ ██║   ██║██╔██╗ ██║█████╔╝ ██║   ██║
██   ██║  ╚██╔╝  ██║   ██║██║╚██╗██║██╔═██╗ ██║   ██║
╚█████╔╝   ██║   ╚██████╔╝██║ ╚████║██║  ██╗╚██████╔╝
 ╚════╝    ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ 
                                                     
    Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    https://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
import OlivOS
import OlivaDiceCore
import flagLoopTest

tmp_reply_str = 'plugin_event != None'

class Event(object):
    def init(self, Proc):
        pass

    def private_message(self, Proc):
        reply(self, Proc)

    def group_message(self, Proc):
        reply(self, Proc)

    def poke(self, Proc):
        pass

    def save(self, Proc):
        pass

    def menu(self, Proc):
        pass


def reply(plugin_event, Proc):
    if plugin_event.data.message[:5] != 'start':
        return
    while True:
        flag_need_loop = False
        if plugin_event != None:
            if flag_need_loop := True:
                OlivaDiceCore.msgReply.replyMsg(plugin_event, tmp_reply_str)
                tmp_select: 'str|None' = OlivaDiceCore.msgReplyModel.replyCONTEXT_regWait(
                    plugin_event=plugin_event, 
                    flagBlock='allowCommand', 
                    hash=OlivaDiceCore.msgReplyModel.contextRegHash([None, plugin_event.data.user_id])
                )
                if type(tmp_select) == str and tmp_select.isdigit():
                    flag_need_loop = False
                    break
            # if plugin_event == None:
            #     plugin_event.reply('plugin_event == None')
            #     break