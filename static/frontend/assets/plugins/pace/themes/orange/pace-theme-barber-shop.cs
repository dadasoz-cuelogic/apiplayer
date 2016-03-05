/* This is a compiled file, you should be editing the file in the templates directory */
.pace {
  -webkit-pointer-events: none;
  pointer-events: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  user-select: none;
}

.pace-inactive {
  display: none;
}

.pace .pace-progress {
  background-color: #eb7a55;
  position: fixed;
  z-index: 2000;
  top: 0;
  left: 0;
  height: 12px;
  overflow: hidden;

  -webkit-transition: width 1s;
  -moz-transition: width 1s;
  -o-transition: width 1s;
  transition: width 1s;
}

.pace .pace-progress-inner {
  position: absolute;
  top: 0;
  left: 0;
  right: -32px;
  bottom: 0;

  background-image: -webkit-gradient(linear, 0 100%, 100% 0, color-stop(0.25, rgba(255, 255, 255, 0.2)), color-stop(0.25, transparent), color-stop(0.5, transparent), color-stop(0.5, rgba(255, 255, 255, 0.2)), color-stop(0.75, rgba(255, 255, 255, 0.2)), color-stop(0.75, transparent), to(transparent));
  background-image: -webkit-linear-gradient(45deg, rgba(255, 255, 255, 0.2) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.2) 50%, rgba(255, 255, 255, 0.2) 75%, transparent 75%, transparent);
  background-image: -moz-linear-gradient(45deg, rgba(255, 255, 255, 0.2) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.2) 50%, rgba(255, 255, 255, 0.2) 75%, transparent 75%, transparent);
  background-image: -o-linear-gradient(45deg, rgba(255, 255, 255, 0.2) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.2) 50%, rgba(255, 255, 255, 0.2) 75%, transparent 75%, transparent);
  background-image: linear-gradient(45deg, rgba(255, 255, 255, 0.2) 25%, transparent 25%, transparent 50%, rgba(255, 255, 255, 0.2) 50%, rgba(255, 255, 255, 0.2) 75%, transparent 75%, transparent);
  -webkit-background-size: 32px 32px;
  -moz-background-size: 32px 32px;
  -o-background-size: 32px 32px;
  background-size: 32px 32px;

  -webkit-animation: pace-stripe-animation 500ms linear infinite;
  -moz-animation: pace-stripe-animation 500ms linear infinite;
  -ms-animation: pace-stripe-animation 500ms linear infinite;
  -o-animation: pace-stripe-animation 500ms linear infinite;
  animation: pace-stripe-animation 500ms linear infinite;
}

@-webkit-keyframes pace-stripe-animation {
  0% { -webkit-transform: none; transform: none; }
  100% { -webkit-transform: translate(-32px, 0); transform: translate(-32px, 0); }
}
@-moz-keyframes pace-stripe-animation {
  0% { -moz-transform: none; transform: none; }
  100% { -moz-transform: translate(-32px, 0); transform: translate(-32px, 0); }
}
@-o-keyframes pace-stripe-animation {
  0% { -o-transform: none; transform: none; }
  100% { -o-transform: translate(-32px, 0); transform: translate(-32px, 0); }
}
@-ms-keyframes pace-stripe-animation {
  0% { -ms-transform: none; transform: none; }
  100% { -ms-transform: translate(-32px, 0); transform: translate(-32px, 0); }
}
@keyframes pace-stripe-animation {
  0% { transform: none; transform: none; }
  100% { transform: translate(-32px, 0); transform: translate(-32px, 0); }
}
