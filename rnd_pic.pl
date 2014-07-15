#!/usr/bin/perl -w

use strict;

	my($back_dir)="/export/home/53759/back";

	show_pic($back_dir, $ARGV[1]) if ($ARGV[1]);

	srand(time ^ $$ ^ unpack "%L*", `ps -ef | gzip`);

	opendir DIR, $back_dir || die "unable to open background image directory\n";
	my(@files)=grep{ /^\w+/ && !/^\.+/ && !/nsfw/ && -f "$back_dir/$_" } readdir(DIR);

	closedir DIR;

	# now randomly choose one.
	
	#my($pic)= $files[rand @files];
	show_pic($back_dir, $files[rand @files]);

sub show_pic {

	my($back_dir)=shift;
	my($pic)=shift;
	my($command);

	# if it says asis dont stretch it.
	if ($pic =~ /asis/i) {
		$command= "/usr/local/bin/xv -root -quit -rmode 5 $back_dir/$pic";
	}
	elsif ($pic =~ /tile/i) {
		$command= "/usr/local/bin/xv -root -quit -rmode 1 $back_dir/$pic";
	}
	else {
		$command="/usr/local/bin/xv -root -quit -max $back_dir/$pic";
	}

	if ($ARGV[0]) {
		$command .= " -display $ARGV[0]";
	}

	system ($command);

	open LOG,">pic.log";
	print LOG "$command\n";
	print LOG "$ENV{'DISPLAY'}\n";
	close LOG;

	exit(0);
}

