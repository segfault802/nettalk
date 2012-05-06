#!/usr/bin/perl



use strict;



my($inputHandle,$outputHandle,@data,$string,$line);

open($inputHandle,"< list.dat");
open($outputHandle,"> out.dat");
close($outputHandle);

while(<$inputHandle>){
	$string .= $_;
	#print $string."\n";
}
@data = split(/ /,$string);
#print @data;
for my $word (@data){
	chomp($word);
	$word = lc($word);
	#print $word." \n";
	$line = "grep \"\^".$word."\\b[ ]*.*\" nettalk.data >> out.dat";
	system($line);
	print $line."\n";
}

print "Hello World!\n";
