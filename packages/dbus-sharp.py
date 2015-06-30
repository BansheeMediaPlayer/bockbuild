class DbusSharpPackage (GitHubPackage):
	def __init__ (self):
		GitHubPackage.__init__ (self, 'mono', 'dbus-sharp', '0.7.0',
			revision = '60cd041dc9676161ed1dcce0652619cad3128159',
			configure = './autogen.sh --prefix="%{prefix}"')

DbusSharpPackage ()
