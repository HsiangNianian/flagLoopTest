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
    def init(plugin_event, Proc):
        pass

    def private_message(plugin_event, Proc):
        reply(plugin_event, Proc)

    def group_message(plugin_event, Proc):
        reply(plugin_event, Proc)

    def poke(plugin_event, Proc):
        pass

    def save(plugin_event, Proc):
        pass

    def menu(plugin_event, Proc):
        if plugin_event.data.namespace == 'OlivOSPluginTemplate':
            if plugin_event.data.event == 'OlivOSPluginTemplate_Menu_001':
                pass
            elif plugin_event.data.event == 'OlivOSPluginTemplate_Menu_002':
                pass


def reply(plugin_event, Proc):
    if plugin_event.data.message[:5] == 'start':
        while True:
            flag_need_loop = False
            if plugin_event != None:
                flag_need_loop = True
                if flag_need_loop:
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