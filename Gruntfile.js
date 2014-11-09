module.exports = function(grunt) {
    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        sass: {
            dist: {
                options: {                       // Target options
                    style: 'compressed'
                },
                files: {
                    'assets/css/foundation.css': 'bower_components/foundation/scss/foundation.scss',
                    'assets/css/normalize.css': 'bower_components/foundation/scss/normalize.scss',
                    'assets/css/styles.css': 'assets/scss/main.scss',
                }
            }
        },

        cssmin: {
          combine: {
            files: {
              'blog/static/css/styles.css': ['assets/css/*.css']
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
                files: ['assets/scss/*.scss'],
                tasks: ['sass']
            },

            uglify: {
                files: ['assets/js/*'],
                tasks: ['uglify']
            },

            cssmin: {
                files: ['assets/css/*.css'],
                tasks: ['cssmin']
            },
        }


    });

    grunt.loadNpmTasks('grunt-contrib-sass');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-cssmin');

    grunt.registerTask('build', ['sass', 'uglify', 'cssmin']);
    grunt.registerTask('default', ['build', 'watch']);
}



// cssmin: {
//   combine: {
//     files: {
//       'path/to/output.css': ['path/to/input_one.css', 'path/to/input_two.css']
//     }
//   }
// }


// cssmin: {
//     my_target: {
//     files: [{
//         expand: true,
//         cwd: 'assets/css/',
//         src: ['*.css', '!*.min.css'],
//         dest: 'blog/static/css/',
//         ext: '.min.css'
//         }]
//     }
// },
