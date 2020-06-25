#!/usr/bin/perl

# This would go into your i3 configuration
#mode "strawberry" {	
#	bindsym Escape [class="strawberry"] kill
#}
#exec --no-startup-id ~/.config/polybar/scripts/i3-signal-mode.pl

use AnyEvent;
use AnyEvent::I3 qw(:all);
my $i3 = i3();

$i3->connect->recv or die "Error connecting";

my %callbacks = (
	window => sub {
		my ($x) = @_;
		my $ev = $x->{change};
		my $class = $x->{container}->{window_properties}->{class};
		if ($ev eq 'focus' && $class eq 'strawberry') {
    		$i3->message(TYPE_COMMAND, "mode strawberry"); }
    	else {
    		$i3->message(TYPE_COMMAND, "mode default"); }
	}
);

$i3->subscribe(\%callbacks)->recv->{success}
	or die "Error subscribing";

AE::cv->recv
