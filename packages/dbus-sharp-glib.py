class DbusSharpGlibPackage (GitHubPackage):
	def __init__ (self):
		GitHubPackage.__init__ (self, 'mono', 'dbus-sharp-glib', '0.5.0',
			revision = '7a2e676e867fec8db6185334d4242ec440895c27',
			configure = './autogen.sh --prefix="%{prefix}"')

DbusSharpGlibPackage ()
