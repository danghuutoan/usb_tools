import usb.core
import usb.util

dev = usb.core.find(find_all=True)

d = dev.next()

print d.get_active_configuration()

