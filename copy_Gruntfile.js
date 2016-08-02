module.exports = function(grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
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
          }
        ]
      }
    },

    watch: {
      copy: {
        files: ['src/*.html'],
        tasks: ['copy']
      }
    }
  });
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-copy');

  grunt.registerTask('default', ['copy']);
};
