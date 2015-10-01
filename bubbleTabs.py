import sublime, sublime_plugin

class bubbleTabs(sublime_plugin.EventListener):  

	def on_activated(self,view):  
		view.window().set_view_index(view.window().active_view(),0,0)

