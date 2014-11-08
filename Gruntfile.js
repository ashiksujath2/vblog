module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),

    uglify: {
      my_target: {
        files: {
          'blog/static/js/libs.min.js': ['bower_components/jquery/dist/jquery.js'],
        }
      }
    },

    watch: {
      grunt: { files: ['Gruntfile.js'] },

      uglify: {
        files: ['js/*'],
        tasks: ['uglify']
      }
    }


  });

  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-watch');

  grunt.registerTask('default', ['uglify', 'watch']);
}
