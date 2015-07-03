class BansheePackage (Package):
	def __init__ (self):
		Package.__init__ (self, 'banshee', '2.6.3', git_branch = 'stable-2.6')

		self.sources = [
			'git://git.gnome.org/banshee',
		]

		self.configure = [ 'NOCONFIGURE=1 ./autogen.sh && ./profile-configure %{profile.name} --prefix=%{prefix}' ]

BansheePackage ()
