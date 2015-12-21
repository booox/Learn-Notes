/*******************************************************************************
 *									       *
 ******************************************************************************/

/*
 *	Copyright:	
 *	name:		DFPlayer_Mini_Mp3 IR mp3 player
 *	Author:		
 *	Date:		2015-12-20
 *	Description:	
 *			note: mp3 file must put into mp3 folder in your tf card
 */

#include <SoftwareSerial.h>
#include <DFPlayer_Mini_Mp3.h>
#include <IRremote.h>


//定义对应16进制数值的常量名
#define POWER   0xFD00FF       //电源
#define VOLUP   0xFD807F       //VOL+
#define FUNC    0xFD40BF       //FUNC/STOP
#define PREV    0xFD20DF       //后退/上一曲
#define PAUSE   0xFDA05F       //暂停/播放
#define NEXT    0xFD609F       //前进/下一曲
#define DOWN    0xFD10EF       //下一页
#define VOLDOWN 0xFD906F       //VOL-
#define UP      0xFD50AF       //上一页
#define ZERO    0xFD30CF       //0
#define EQ      0xFDB04F       //EQ
#define REPT    0xFD708F       //ST/REPT
#define ONE     0xFD08F7       //1
#define TWO     0xFD8877       //2
#define THREE   0xFD48B7       //3
#define FOUR    0xFD28D7       //4
#define FIVE    0xFDA857       //5
#define SIX     0xFD6897       //6
#define SEVEN   0xFD18E7       //7
#define EIGHT   0xFD9867       //8
#define NINE    0xFD58A7       //9

char* buttonNumbers[] = { "ONE", "TWO",  "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int RECV_PIN = 11;
IRrecv irrecv(RECV_PIN);
decode_results results;

// mp3 player v
int mp3Volume = 15;
boolean playFlag = true;
boolean singleAllMode = true;


//
void setup () {
	Serial.begin (9600);
	mp3_set_serial (Serial);	//set Serial for DFPlayer-mini mp3 module 
	delay(1);  //wait 1ms for mp3 module to set volume
	mp3_set_volume (mp3Volume);
	mp3_all_loop(singleAllMode);
	irrecv.enableIRIn(); // Start the receiver
}


//
void loop () {        
	
	if (irrecv.decode(&results)) {
		Serial.println(results.value, HEX);
		// irrecv.resume(); // Receive the next value
		
		// Power
		if(results.value == POWER){
			if(playFlag){
				mp3_stop();
			}
			else{
				mp3_play();
			}
			playFlag = ! playFlag;
			
		}
		
		// single mode & all mode
		if(results.value == FUNC){
			if(singleAllMode){
				mp3_all_loop(singleAllMode);
			}
			else{
				mp3_single_loop(!singleAllMode);
			}
			playFlag = ! singleAllMode;
			
		}
		
		//VOL+
		if(results.value == VOLUP){
			// mp3Volume = mp3_get_volume ();
			mp3Volume = constrain(mp3Volume + 1, 0, 30);
			mp3_set_volume(mp3Volume);
			
		}
		
		//VOL-
		if(results.value == VOLDOWN){
			// mp3Volume = mp3_get_volume ();
			mp3Volume = constrain(mp3Volume - 1, 0, 30);
			mp3_set_volume(mp3Volume);
		}
		
		//PREV
		if(results.value == PREV){
			mp3_prev ();
		}
		
		//NEXT
		if(results.value == NEXT){
			mp3_next ();
		}
		
		//PAUSE
		if(results.value == PAUSE){
			if(playFlag){
				mp3_pause ();
			}
			else{
				mp3_play();
			}
			playFlag = ! playFlag;
			
		}
		
		//ONE ~ NINE
		if(results.value == ONE){
			mp3_play (1);
		}
		if(results.value == TWO){
			mp3_play (2);
		}
		if(results.value == THREE){
			mp3_play (3);
		}
		if(results.value == FOUR){
			mp3_play (4);
		}
		if(results.value == FIVE){
			mp3_play (5);
		}
		if(results.value == SIX){
			mp3_play (6);
		}
		if(results.value == SEVEN){
			mp3_play (7);
		}
		if(results.value == EIGHT){
			mp3_play (8);
		}
		if(results.value == NINE){
			mp3_play (9);
		}
		

		irrecv.resume(); // Receive the next value
	  }	
	
}

/*
   mp3_play ();		//start play
   mp3_play (5);	//play "mp3/0005.mp3"
   mp3_next ();		//play next 
   mp3_prev ();		//play previous
   mp3_set_volume (uint16_t volume);	//0~30
   mp3_set_EQ ();	//0~5
   mp3_pause ();
   mp3_stop ();
   void mp3_get_state (); 	//send get state command
   void mp3_get_volume (); 
   void mp3_get_u_sum (); 
   void mp3_get_tf_sum (); 
   void mp3_get_flash_sum (); 
   void mp3_get_tf_current (); 
   void mp3_get_u_current (); 
   void mp3_get_flash_current (); 
   void mp3_single_loop (boolean state);	//set single loop 
   void mp3_all_loop (boolean state);	//set all loop 
   void mp3_DAC (boolean state); 
   void mp3_random_play (); 
 */