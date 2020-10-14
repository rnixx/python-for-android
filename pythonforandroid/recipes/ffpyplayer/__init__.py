from pythonforandroid.recipe import CythonRecipe
from pythonforandroid.toolchain import Recipe
from os.path import join


class FFPyPlayerRecipe(CythonRecipe):
    version = 'f612407b37606854cf466fbc0a7cc8a5fe7f3ea7'
    url = 'https://github.com/rnixx/ffpyplayer/archive/{version}.zip'
    # version = 'v4.3.1'
    # url = 'https://github.com/matham/ffpyplayer/archive/{version}.zip'
    depends = ['python3', 'sdl2', 'ffmpeg']
    opt_depends = ['openssl', 'ffpyplayer_codecs']

    def get_recipe_env(self, arch, with_flags_in_cc=True):
        env = super().get_recipe_env(arch)

        build_dir = Recipe.get_recipe('ffmpeg', self.ctx).get_build_dir(arch.arch)
        env["FFMPEG_INCLUDE_DIR"] = join(build_dir, "include")
        env["FFMPEG_LIB_DIR"] = join(build_dir, "lib")
        # env["FFMPEG_DISABLE_GPL"] = '1'
        env["CONFIG_POSTPROC"] = '0'

        env["SDL_INCLUDE_DIR"] = join(self.ctx.bootstrap.build_dir, 'jni', 'SDL', 'include')
        env["SDL_LIB_DIR"] = join(self.ctx.bootstrap.build_dir, 'libs', arch.arch)

        env["USE_SDL2_MIXER"] = '1'
        env["SDL2_MIXER_INCLUDE_DIR"] = join(self.ctx.bootstrap.build_dir, 'jni', 'SDL2_mixer')

        print(80 * '#')
        print(env['LDFLAGS'])
        print(80 * '#')

        return env


recipe = FFPyPlayerRecipe()
