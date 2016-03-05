/* This is a compiled file, you should be editing the file in the templates directory */
.pace {
  -webkit-pointer-events: none;
  pointer-events: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
}

.pace.pace-inactive .pace-progress {
  display: none;
}

.pace .pace-progress {
  position: fixed;
  z-index: 2000;
  top: 0;
  right: 0;
  height: 5rem;
  width: 5rem;
}

.pace .pace-progress:after {
  display: block;
  position: absolute;
  top: 0;
  right: .5rem;
  content: attr(data-progress-text);
  font-family: "Helvetica Neue", sans-serif;
  font-weight: 100;
  font-size: 5rem;
  line-height: 1;
  text-align: right;
  color: rgba(124, 96, 224, 0.19999999999999996);
}
