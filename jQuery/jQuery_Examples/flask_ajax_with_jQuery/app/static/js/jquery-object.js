$(function() {
	var headings = $("h1");
	console.log( "headings count:" + headings.length );

	var firstHeading = headings.eq(0);
	var firstHeading_1 = headings.eq(0);

	console.log ( $("h1") == $("h1") );
	console.log( $("h1").position() );

	console.log( '---------------' )
	
	var myArray = [1, 2, 3, 4, 5, 'abc', 'tt', 9]
	if ( $.inArray(4, myArray) !== -1 ){
		console.log( "found it!" );
	}
	if ( $.inArray('abc', myArray) !== -1 ){
		console.log( "found it!" );
	}

	console.log( '---------------' )

	console.log( $("h1").css( "fontSize" ));
	console.log( $("h1").css( "fontsize" ));
	console.log( $("h1").css( "font-size" ));

	$("h1").css("font-size",  "34px");
	console.log( $("h1").css( "font-size" ));
	$("h1").css({
		"font-size": "50px",
		color: "red"
	});
	console.log( $("h1").css( "font-size" ));
	console.log( $("h1").css( "color" ));

	console.log( $("h1").width() );
	console.log( $("h1").height() );
	console.log( $("h1").position() );

	$("#myDiv").data("keyName", {foo: "bar"});
	console.log( $("#myDiv").data("keyName") );
	$("#myDiv").data("keyName", "hhahahaha text");
	console.log( $("#myDiv").data("keyName") );
	console.log( $("#myDiv").data("keyiame") );

	console.log( '---------------' )

	$.each(["foo", "bar", "baz"], function( idx, val ){
		console.log( "element " + idx + " is " + val );
	});

	console.log( '---------------' )

	$.each({foo: "bar", baz: "bim" }, function( k, v ){
		console.log( k + " : " + v );
	});
});
