module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        sass: {
            dist: {
                options: {                       // Target options
                    style: 'compressed'
                },
                files: {
                    'css/styles.css': 'scss/main.scss',
                }
            }
        },

        less: {
            dist: {
                options: {

                },
                files: {
                    'css/bootstrap.css': 'bower_components/bootstrap/less/bootstrap.less',
                    'css/main.css': 'less/main.less',
                }
            }
        },

        cssmin: {
          combine: {
            files: {
              '../src/assets/css/styles.min.css': [
                'css/*.css',
                'bower_components/google-code-prettify/bin/prettify.min.css'
                ]
            }
          }
        },

        uglify: {
            my_target: {
                files: {
                  '../src/assets/js/libs.min.js': [
                    'bower_components/jquery/dist/jquery.js',
                    'bower_components/bootstrap/dist/js/bootstrap.js',
                    'bower_components/google-code-prettify/bin/prettify.min.js',
                    'js/clean-blog.js'],
                }
            }
        },

        watch: {
            grunt: { files: ['Gruntfile.js'] },

            // sass: {
            //     files: ['scss/*.scss'],
            //     tasks: ['sass']
            // },

            less: {
                files: ['less/*.less'],
                tasks: ['less']
            },

            uglify: {
                files: ['js/*'],
                tasks: ['uglify']
            },

            cssmin: {
                files: ['css/*.css'],
                tasks: ['cssmin']
            },
        }


    });

    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-less');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-cssmin');

    grunt.registerTask('build', ['less', 'uglify', 'cssmin']);
    grunt.registerTask('default', ['build', 'watch']);
};



