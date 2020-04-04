from subscriber import AgriIOTSubscriber
from database import AgriIOTDatabase

sub = AgriIOTSubscriber()
#sub_path = sub.createSubscription("main_sub", "main")
sub_path = sub.getExistingSubscriptionPath("main_sub")
sub.subscribe(sub_path)
