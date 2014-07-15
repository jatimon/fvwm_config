#!/usr/bin/perl

# cheap and dirty output AddToMenu stuff for weather in fvwm

$DATE=`date`;
chomp $DATE;
print "DestroyMenu recreate MenuFvwmWeather\n";
print "AddToMenu MenuFvwmWeather \"$DATE\" Title\n";

while ($line = <>) {
	chomp $line;
	$line =~ s/<title>spacer//;
	$line =~ /<title>(.*)<\/title>/ and print "+ \"\" Nop\n+ \"$1\"\n";
	if ($line =~ /<description>/) { 
		push @ary, $line;
		while ($line = <>) {
			push @ary, $line;
			$line =~ /<\/description>/ and last;
		}				
		
		$str = join '' , @ary;
		#print "+ \"$str\"\n" ;
		$str =~ s/\n*//g;
		$str =~ s/\&amp\;nbsp\;\&amp\;deg\;/ /g;
		$str =~ s/\s\s+/ /g;
		$str =~ s/\s+<description>\s*/\+ \"/;
		$str =~ s/\,/\"\n+ \"/g;
		$str =~ s/\s*<\/description>/\"\n/;
		print "$str" ;
	}
	@ary="";
}


#print "ChangeMenuStyle Weather MenuFvwmWeather\n";
