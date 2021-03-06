module.exports = function(grunt) {

  // Project configuration
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    concat: {
      options: {
        //define a string to seperate files in the concatenated output
        seperator: ';'
      },
      dist1: {
        //the files to concatenate
        src: ['src/js/custom/*.js'],
        //the location of the resulting JS file
        dest: 'src/js/<%= pkg.name %>.js'
      },
      dist2: {
        //the files to concatenate
        src: ['src/js/bootstrap/*.js'],
        //the location of the resulting JS file
        dest: 'src/js/bootstrap.js'
      }
    },
    uglify: {
      options: {
        preserveComments: "some"
      },
      dist: {
        files: [
          {
            expand: true,
            cwd:    "src/js/",
            src:    ["*.js"],
            dest:   "dist/js/",
            ext:    ".min.js",
            extDot: "first"
          }
        ],
      }
    },
    less: {
      expanded: {
        files: [
          {
            expand: true,
            cwd:    "src/less/",
            src:    ["*.less"],
            dest:   "src/css/",
            ext:    ".css",
            extDot: "first"
          }
        ]

      },
      minified: {
        options: {
          paths: ["css"],
          cleancss: true
        },
        files: [
          {
            expand: true,
            cwd:    "src/css/",
            src:    ["*.css"],
            dest:   "dist/css/",
            ext:    ".min.css",
            extDot: "first"
          }
        ]
      }
    },
    copy: {
      main: {
        files: [
          {
            expand: true,
            cwd:    "src/",
            src:    ["*.html"],
            dest:   "dist/",
            ext:    ".html",
            extDot: "first"
          },
          {
            expand: true,
            cwd:    "src/",
            src:    ["*.php"],
            dest:   "dist/",
            ext:    ".php",
            extDot: "first"
          },
        ]
      },
      testsite: {
      //In the test/debug folder build a working version of the site with un-minified css an js to make testing with browser tools easier
        files: [
          {
            expand: true,
            cwd:    "src/css/",
            src:    ["*.css"],
            dest:   "test/debug/css/",
            ext:    ".min.css",
            extDot: "first"
          },
          {
            expand: true,
            cwd:    "src/js/",
            src:    ["*.js"],
            dest:   "test/debug/js/",
            ext:    ".min.js",
            extDot: "first"
          },
          {
            expand: true,
            cwd:    "src/",
            src:    ["*.html"],
            dest:   "test/debug/",
            ext:    ".html",
            extDot: "first"
          }
        ]
      }
    },
    qunit: {
      files: ['test/*.html', 'test/bootstrap/index.html']
    },
    jshint: {
      // define the files to lint
      files: ['Gruntfile.js', 'src/**/*.js', 'test/*.js'],
      // configure JSHint (documented at http://www.jshint.com/docs/)
      options: {
        // more options here if you want to override JSHint defaults
        jshintrc: true
      }
    },
    watch: {
      scripts: {
        files: ['src/js/**/*.js'],
        tasks: ['concat', 'uglify', 'jshint', 'qunit']
      },
      less: {
        files: ['src/less/**/*.less'],
        tasks: ['less'],
        options: {
          spawn: false,
        }
      },
      copy: {
        files: ['src/*.html', 'src/*.php'],
        tasks: ['copy:main']
      }
    }
  });
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-qunit');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-copy');
  grunt.loadNpmTasks('grunt-contrib-concat');

  // this would be run by typing "grunt test" on the command line
  grunt.registerTask('test', ['jshint', 'qunit']);

  // the default task can be run just by typing "grunt" on the command line
  grunt.registerTask('default', ['jshint', 'qunit', 'concat', 'uglify', 'less','copy:main']);
  grunt.registerTask('testsite', ['copy:testsite']);
};
