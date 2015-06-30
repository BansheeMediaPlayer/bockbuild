class BansheePackage (Package):
	def __init__ (self):
		Package.__init__ (self, 'banshee', '2.6.3', git_branch = 'stable-2.6')

		self.sources = [
			'git://git.gnome.org/banshee',
			# workaround against broken gtk_reparent_*  on gtk-quartz
			'https://github.com/Dynalon/banshee-osx/commit/798ba9ad74f91b1bc9e7ad7c36d6044fceb7a1d5.diff',

			# fix configure complaining about missing HAVE_DBUS_GLIB conditional
			'patches/banshee-fix-dbus-conditional.patch',

		]

		self.configure = [ 'NOCONFIGURE=1 ./autogen.sh && ./profile-configure %{profile.name} --prefix=%{prefix}' ]

	def prep (self):
		Package.prep (self)
		#for p in range (1, len (self.sources)):
		#	self.sh ('patch -p1 < "%{sources[' + str (p) + ']}"')
		self.sh ('patch -p1 < "%{sources[1]}"')
		self.sh ('patch -p0 < "%{sources[2]}"')

BansheePackage ()
