# Activate Headless Display (Xvfb)
# Initial version copied from:
# https://github.com/seleniumbase/SeleniumBase/blob/3f60c2e0fd78807528661aff36120700d4ff1ed6/integrations/linux/Xvfb_launcher.sh

sudo Xvfb -ac :99 -screen 0 1280x1024x16 > /dev/null 2>&1 &
export DISPLAY=:99
exec "$@"