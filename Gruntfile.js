module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        sass: {
            dist: {
                options: {                       // Target options
                    style: 'compressed'
                },
                files: {
                    'blog/static/css/styles.css': 'assets/scss/main.scss',
                }
            }
        },

        uglify: {
            my_target: {
                files: {
                  'blog/static/js/libs.min.js': ['bower_components/jquery/dist/jquery.js'],
                }
            }
        },

        watch: {
            grunt: { files: ['Gruntfile.js'] },

            sass: {
                files: ['scss/**/*.scss'],
                tasks: ['sass']
            },

            uglify: {
                files: ['js/*'],
                tasks: ['uglify']
            }
        }


    });

    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-watch');

    grunt.registerTask('build', ['sass', 'uglify']);
    grunt.registerTask('default', ['build', 'watch']);
}
