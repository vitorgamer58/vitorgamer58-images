#include <EtherCard.h>


static byte mymac[] = { 0x74,0x69,0x69,0x2D,0x30,0x31 };
static byte myip[] = {192,168,0,177};
byte Ethernet::buffer[500];
byte ThisByte;
BufferFiller bfill;
static word homePage4(){
bfill = ether.tcpOffset();
bfill.emit_p(PSTR(
"HTTP/1.0 503 Service Unavailable\r\n"
"Content-Type: text/html\r\n"
"Retry-After: 600\r\n"
"\r\n"
"<html>"
  "<head><title>"
    "Teste-Homepage"
  "</title></head>"
  "<body>"
    "<h3>Teste de Web Server</h3>"
    "<p><em>"
      "Carregado com sucesso!!!<br />"
      "LED AZUl"
    "</em></p>"
  "</body>"
"</html>"
));
return bfill.position();
}
void setup() {
  pinMode(9, OUTPUT);
  if (ether.begin(sizeof Ethernet::buffer, mymac, 8) == 0);
  else
  ether.staticSetup(myip);
}

void loop(){
  word pos = ether.packetLoop(ether.packetReceive());
  if(pos){
   if (Ethernet::buffer[59]==100){ //97 = a , LED azul
     digitalWrite(9, HIGH);
     delay(90);
     digitalWrite(9, LOW);
     ether.httpServerReply(homePage4());
   }
   else {
    digitalWrite(9, LOW);
  }
    
   
   
  }
}
