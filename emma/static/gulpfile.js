var gulp = require('gulp');
var stylus = require('gulp-stylus');
var nib = require('nib');
var nanoCSS = require('gulp-cssnano');
var nunjucksRender = require('gulp-nunjucks-render');
var prettify = require('gulp-prettify');

var config = {
  styles: {
    main: './styl/main.styl',
    root: './styl/**/*.styl',
    output: './css'
  },
}

gulp.task('build:css', function () {
  gulp.src(config.styles.main)
    .pipe(stylus({
      use: nib(),
      'include css': true
    }))
    //.pipe(nanoCSS())
    .pipe(gulp.dest(config.styles.output));
})

gulp.task('nunjucks', function () {
  return gulp.src('templates/*.html')
    .pipe(nunjucksRender({
      path: ['templates/']
    }))
    .pipe(gulp.dest('.'));
});

gulp.task('watch', function () {
  gulp.watch(config.styles.root, ['build:css']);
  gulp.watch('./templates/**/*', ['nunjucks']);
})

gulp.task('default', ['watch', 'build:css', 'nunjucks'])
