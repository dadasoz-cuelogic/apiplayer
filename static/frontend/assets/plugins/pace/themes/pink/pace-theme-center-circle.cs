/* This is a compiled file, you should be editing the file in the templates directory */
.pace {
  -webkit-pointer-events: none;
  pointer-events: none;

  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;

  -webkit-perspective: 12rem;
  -moz-perspective: 12rem;
  -ms-perspective: 12rem;
  -o-perspective: 12rem;
  perspective: 12rem;

  z-index: 2000;
  position: fixed;
  height: 6rem;
  width: 6rem;
  margin: auto;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.pace.pace-inactive .pace-progress {
  display: none;
}

.pace .pace-progress {
  position: fixed;
  z-index: 2000;
  display: block;
  position: absolute;
  left: 0;
  top: 0;
  height: 6rem;
  width: 6rem !important;
  line-height: 6rem;
  font-size: 2rem;
  border-radius: 50%;
  background: rgba(233, 15, 146, 0.8);
  color: #fff;
  font-family: "Helvetica Neue", sans-serif;
  font-weight: 100;
  text-align: center;

  -webkit-animation: pace-3d-spinner linear infinite 2s;
  -moz-animation: pace-3d-spinner linear infinite 2s;
  -ms-animation: pace-3d-spinner linear infinite 2s;
  -o-animation: pace-3d-spinner linear infinite 2s;
  animation: pace-3d-spinner linear infinite 2s;

  -webkit-transform-style: preserve-3d;
  -moz-transform-style: preserve-3d;
  -ms-transform-style: preserve-3d;
  -o-transform-style: preserve-3d;
  transform-style: preserve-3d;
}

.pace .pace-progress:after {
  content: attr(data-progress-text);
  display: block;
}

@-webkit-keyframes pace-3d-spinner {
  from {
    -webkit-transform: rotateY(0deg);
  }
  to {
    -webkit-transform: rotateY(360deg);
  }
}

@-moz-keyframes pace-3d-spinner {
  from {
    -moz-transform: rotateY(0deg);
  }
  to {
    -moz-transform: rotateY(360deg);
  }
}

@-ms-keyframes pace-3d-spinner {
  from {
    -ms-transform: rotateY(0deg);
  }
  to {
    -ms-transform: rotateY(360deg);
  }
}

@-o-keyframes pace-3d-spinner {
  from {
    -o-transform: rotateY(0deg);
  }
  to {
    -o-transform: rotateY(360deg);
  }
}

@keyframes pace-3d-spinner {
  from {
    transform: rotateY(0deg);
  }
  to {
    transform: rotateY(360deg);
  }
}
