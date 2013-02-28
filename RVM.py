import sublime, sublime_plugin, os

def getRvmHome():
  rvm_home = None
  availiable_paths = [
    os.environ['HOME'] + '/.rvm',
    '/usr/local/rvm'
  ]
  for path in availiable_paths:
    if os.path.isfile(path + '/bin/rvm'):
      rvm_home = path
      break
  return rvm_home

RVM_HOME = getRvmHome()
RUBY_PATHS = {
  0: "ruby",
  1: RVM_HOME + "/bin/ruby",
  2: RVM_HOME + "/bin/rvm-auto-ruby"
}

class EnableRvmCommand(sublime_plugin.ApplicationCommand):
  def run(self, type=0):
    ruby_path = RUBY_PATHS[type]
    s = sublime.load_settings("Ruby.sublime-build")
    s.set("cmd", [ruby_path, "$file"])
    s.set("file_regex", "^(...*?):([0-9]*):?([0-9]*)")
    s.set("selector", "source.ruby")
    sublime.save_settings("Ruby.sublime-build")
