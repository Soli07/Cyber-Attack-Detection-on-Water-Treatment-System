html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Water Treatment</title>
    </head>
    <body>
    <?php include 'data.php'; ?>
    
    
        <img src="water treatment images/water tank.jpeg" alt="Water Tank" style="position: absolute; top: 130px; left: 145px; width: 100px; height: 100px;">
        <p style="position: absolute; top: 220px; left:150px; color: darkblue;"> Raw Water Tank</p>

        <img src="water treatment images/raw water pump.jpeg" alt="Pump 1" style="position: absolute; top: 50px; left: 300px; width: 100px; height: 100px;">
        <div id="p101" style="position: absolute; top:60px; left:300px; color: darkblue; font-size:10px"></div>

        <img src="water treatment images/raw water pump.jpeg" alt="Pump 2" style="position: absolute; top: 200px; left: 300px; width: 100px; height: 100px;">
        <div id="p102" style="position: absolute; top:205px; left:380px; color: darkblue; font-size:10px"></div>
        <p style="position: absolute; top: 280px; left: 300px; color: darkblue;">Raw Water Pumps</p>


        <img src="water treatment images/chemical tank.jpeg" alt="chemicals tank 1" style="position: absolute; top: 240px; left: 500px; width: 100px; height: 100px;">
        <p style="position: absolute; top: 330px; left: 520px; color: darkblue;">NaCl Tank</p>

        <img src="water treatment images/chemical tank.jpeg" alt="chemicals tank 2" style="position: absolute; top: 240px; left: 605px; width: 100px; height: 100px;">
        <p style="position: absolute; top: 330px; left: 630px; color: darkblue;">HCL Tank</p>

        <img src="water treatment images/chemical tank.jpeg" alt="chemicals tank 3" style="position: absolute; top: 240px; left: 710px; width: 100px; height: 100px;">
        <p style="position: absolute; top: 330px; left: 740px; color: darkblue;">NaOCl Tank</p>

         <img src="water treatment images/chem dosing valve.jpeg" alt="valve with actuator" style="position: absolute; top: 40px; left:30px; width: 100px; height: 100px;">
         <p style="position: absolute; top:55px; left:6px; color: darkblue;">Feed<br> Water</p>
         <p style="position: absolute; top:110px; left:50px; color: darkblue;font-size: 12px">Raw water<br>Inlet valve</p>
        <div id="mv101" style="position: absolute; top:95px; left:60px; color: darkblue; font-size:10px"></div>
        
        
        <img src="water treatment images/uf level meter 1012.png" alt="sensor reading" style="position: absolute; top:48px; left:175px; width: 100px; height: 100px;">
        <p style="position: absolute; top:43px; left:200px; color: darkblue;font-size: 9px">Raw water<br>Level Meter</p>
        <div id="lit101" style="position: absolute; top:63px; left:205px; color: darkblue; font-size:10px"></div>

        <img src= "water treatment images/static mixer.jpeg" alt="static mixer 1" style="position: absolute; top:130px; left:810px; width: 100px; height: 100px;">
        <p style="position: absolute; top:180px; left:841px; color: darkblue;font-size:12px">Static Mixer</p>

        <img src="water treatment images/chem dosing valve.jpeg" alt="valve with actuator 2" style="position: absolute; top:120px; left:890px; width: 100px; height: 100px;">
        <div id="mv201" style="position: absolute; top:175px; left:925px; color: darkblue; font-size:10px"></div>

         <p style="position: absolute; top:185px; left:927px; color: darkblue;font-size:10px">Chem<br>Dosing <br>Valve</p>


         <img src= "water treatment images/water tank.jpeg" alt="UFFeed WaterTank" style="position: absolute; top:210px; left: 950px; width: 100px; height: 100px;">
         <p style="position: absolute; top:300px; left:973px; color: darkblue;font-size:15px">UF Feed<br>Water Tank</p>


          <img src="water treatment images/uf level meter 1012.png" alt="sensor reading 2" style="position: absolute; top:100px; left: 970px; width: 100px; height: 100px;">
          <p style="position: absolute; top:80px; left:1000px; color: darkblue;font-size:10px">UF Feed<br>Level Meter</p>
        <div id="lit301" style="position: absolute; top:105px; left:1005px; color: darkblue; font-size:10px"></div>
        <img src="water treatment images/raw water pump.jpeg" alt="Pump 3" style="position: absolute; top:166px; left:1100px; width: 100px; height: 100px;">
        <div id="p301" style="position: absolute; top:176px; left:1179px; color: darkblue;font-size:15px"></div>


         <img src="water treatment images/raw water pump.jpeg" alt="Pump 4" style="position: absolute; top:267px; left:1100px; width: 100px; height: 100px;">
         <div id="p302" style="position: absolute; top:277px; left:1179px; color: darkblue;font-size:15px"></div>
         <p style="position: absolute; top:340px; left:1110px; color: darkblue;">UF Feed Pumps</p>


        <img src="water treatment images/uf membrane.jpeg" alt="uf membrane" style="position: absolute; top:168px; left:1291px; width: 100px; height: 100px;">
         <p style="position: absolute; top:230px; left:1355px; color: darkblue;font-size:10px">UF<br> Membrane</p>


        <img src="water treatment images/chem dosing valve.jpeg" alt="Valve with actuator 3" style="position: absolute; top:95px; left:1340px; width: 100px; height: 100px;">
         <div id="mv302" style="position: absolute; top:150px; left:1373px; color: darkblue;font-size:10px"></div>
         <p style="position: absolute; top:160px; left:1373px; color: darkblue;font-size:10px">RO Feed<br>Valve</p>


        <img src="water treatment images/water tank.jpeg" alt="RO feed water tank" style="position: absolute; top:190px; left:1410px; width: 100px; height: 100px;">
        <p style="position: absolute; top:276px; left:1432px; color: darkblue;font-size:15px">RO Feed<br>WaterTank</p>


        <img src="water treatment images/raw water pump.jpeg" alt="pump 5" style="position: absolute; top:247px; left:1589px; width: 100px; height: 100px;">
         <div id="p401" style="position: absolute; top:257px; left:1671px; color:darkblue;font-size:15px"></div>



        <img src="water treatment images/raw water pump.jpeg" alt="pump 6" style="position: absolute; top:147px; left:1589px; width: 100px; height: 100px;">
         <div id="p402" style="position: absolute; top:157px; left:1671px; color: darkblue;font-size:15px"></div>


        <img src="water treatment images/rofeed level meter 1008.jpeg" alt="sensor reading 3" style="position: absolute; top:90px; left:1426px; width: 100px; height: 100px;">
         <p style="position: absolute; top:63px; left:1460px; color: darkblue;font-size:10px">ROFeed<br>LevelMeter</p>
         <div id="lit401" style="position: absolute; top:87px; left:1463px; color: darkblue;font-size:10px"></div>


        <img src="water treatment images/uv dechlor.jpeg" alt="uv dechlorinator" style="position: absolute; top:494px; left:1740px; width: 100px; height: 100px;">
        <p style="position: absolute; top:540px; left:1750px; color: darkblue;font-size:13px">UV_Dechlorinator</p>

        <img src="water treatment images/static mixer.jpeg" alt="static mixer 2" style="position: absolute; top:440px; left:1610px; width: 100px; height: 100px;">
         <p style="position: absolute; top:486px; left:1650px; color: darkblue;font-size:14px">Static Mixer</p>


        <img src="water treatment images/chemical tank.jpeg" alt="chemicals tank 4" style="position: absolute;top:607px;left:1680px; width: 100px; height: 100px;">
        <p style="position: absolute; top:695px; left:1695px; color: darkblue;font-size:14px">NAHSO3_Tank</p>


         <img src="water treatment images/filter.jpeg" alt="filter tank" style="position: absolute;top:515px;left:1562px; width: 100px; height: 100px;">
         <p style="position: absolute; top:583px; left:1597px; color: darkblue;font-size:14px">Filter</p>


         <img src="water treatment images/raw water pump.jpeg" alt="pump 7" style="position: absolute;top:465px;left:1353px; width: 100px; height: 100px;">
         <div id="p501" style="position: absolute; top:475px; left:1435px; color: darkblue;font-size:14px"></div>


         <img src="water treatment images/raw water pump.jpeg" alt="pump 8" style="position: absolute;top:563px; left:1353px; width: 100px; height: 100px;">
         <div id="p502" style="position: absolute; top:575px; left:1435px; color: darkblue;font-size:14px"></div>

         <img src="water treatment images/vessels.jpeg" alt="RO Vessels 1" style="position: absolute;top:550px; left:1149px; width: 100px; height: 100px;">


         <img src="water treatment images/vessels.jpeg" alt="RO Vessels 2" style="position: absolute;top:620px; left:1149px; width: 100px; height: 100px;">


         <img src="water treatment images/vessels.jpeg" alt="RO Vessels 3" style="position: absolute;top:690px; left:1149px; width: 100px; height: 100px;">

          <img src="water treatment images/chem dosing valve.jpeg" alt="Valve with actuator 4" style="position: absolute; top:605px; left:690px; width: 100px; height: 100px;">
          <p style="position: absolute; top:660px; left:725px; color: darkblue;font-size:10px">MV-501</p>
          <p style="position: absolute; top:670px; left:725px; color: darkblue;font-size:10px">RO Permeate<br>Valve</p>
        
          <img src="water treatment images/blue tank.jpeg" alt="RO Permeate Tank" style="position: absolute; top:625px; left:448px; width: 100px; height: 100px;">
           <p style="position: absolute; top:670px; left:540px; color: darkblue;font-size:15px">RO Permeate<br>Tank</p>
        
          <img src="water treatment images/blue tank.jpeg" alt="CIP Tank" style="position: absolute; top:490px; left:448px; width: 100px; height: 100px;">
          <p style="position: absolute; top:540px; left:540px; color: darkblue;font-size:15px">CIP Tank</p>
          
          
          <img src="water treatment images/raw water pump.jpeg" alt="CIP Pump" style="position: absolute;top:505px; left:313px; width: 100px; height: 100px;">
           <p style="position: absolute; top:515px; left:395px; color: darkblue;font-size:14px">P-603</p>
            <p style="position: absolute; top:575px; left:335px; color: darkblue;font-size:14px">CIP Pump</p>
           
          
          <img src="water treatment images/raw water pump.jpeg" alt="RO Permeate Pump" style="position: absolute;top:635px; left:313px; width: 100px; height: 100px;">
           <p style="position: absolute; top:645px; left:395px; color: darkblue;font-size:14px">P-601</p>
           <p style="position: absolute; top:705px; left:335px; color: darkblue;font-size:14px">RO Permeate<br>Pump</p>
        
         <img src="water treatment images/blue tank.jpeg" alt="UF Backwash Tank" style="position: absolute; top:800px; left:248px; width: 100px; height: 100px;">
         <p style="position: absolute; top:850px; left:340px; color:darkblue;font-size:15px">UF Backwash<br>Tank</p>
         
        
         <img src="water treatment images/raw water pump.jpeg"  alt="UF Backwash Pump" style="position: absolute; top:810px; left:138px; width: 100px; height: 100px;">
         <p style="position: absolute; top:818px; left:220px; color: darkblue;font-size:14px">P-601</p>
        <p style="position: absolute; top:792px; left:100px; color:darkblue;font-size:15px">UF Backwash<br>Pump</p>
         
         
         <img src="water treatment images/chem dosing valve.jpeg" alt="Valve with actuator 5" style="position: absolute; top:95px; left:1245px; width: 100px; height: 100px;">
         <p style="position: absolute; top:150px; left:1280px; color: darkblue;font-size:10px">MV-301</p>
         <p style="position: absolute; top:160px; left:1280px; color: darkblue;font-size:10px">UF Backwash<br>Valve</p>
         
         
          <img src="water treatment images/chem dosing valve.jpeg" alt="Valve with actuator 6" style="position: absolute;top:780px; left:900px; width: 100px; height: 100px;">
         <p style="position: absolute; top:835px; left:935px; color: darkblue;font-size:10px">MV-502</p>
         <p style="position: absolute; top:845px; left:935px; color: darkblue;font-size:10px">BackWash<br>Valve</p>
         
         
         <img src="water treatment images/WhatsApp Image 2024-03-02 at 8.08.45 PM.jpeg"alt="Valve with actuator 7" style="position: absolute;top:680px; left:820px; width: 100px; height: 100px;">
         <p style="position: absolute; top:705px; left:884px; color: darkblue;font-size:10px">MV-503</p>
         <p style="position: absolute; top:715px; left:884px; color: darkblue;font-size:10px">RO Permeate<br>Valve</p>


        <p style="position: absolute; top:65px; left:140px; color: darkblue;font-size:10px">FIT-101</p>
         <p style="position: absolute; top: 150px; left: 600px; color: darkblue;font-size:13px">FIT-201</p>
         <p style="position: absolute; top: 150px; left: 670px; color: darkblue;font-size:13px">ALT-201</p>
         <p style="position: absolute; top:130px; left:925px; color: darkblue;font-size:10px">ALT-202</p>
         <p style="position: absolute; top:155px; left:965px; color: darkblue;font-size:10px">ALT-203</p>
         <p style="position: absolute; top:215px; left:1740px; color:darkblue;font-size:15px">FIT_401</p>
          <p style="position: absolute; top:465px; left:1605px; color: darkblue;font-size:10px">ALT_402</p>
         <p style="position: absolute; top:540px; left:1515px; color: darkblue;font-size:12px">ALT_503</p>
         <p style="position: absolute; top:635px; left:650px; color: darkblue;font-size:12px">ALT_504</p>

        <div style="overflow-x: auto; white-space: nowrap;">
        <svg width="2000" height="150%" style="position: absolute; top: 0; left: 0;">
    
                <line x1="270" y1="180" x2="230" y2="180" style="stroke:grey;stroke-width:2" />
    
                <line x1="321" y1="105" x2="270" y2="105" style="stroke:grey;stroke-width:2" />
                <line x1="420" y1="105" x2="385" y2="105" style="stroke:grey;stroke-width:2" />
    
                 <line x1="420" y1="255" x2="385" y2="255" style="stroke:grey;stroke-width:2" />
                <line x1="270" y1="255" x2="321" y2="255" style="stroke:grey;stroke-width:2" />
    
                 <line x1="420" y1="255" x2="420" y2="105" style="stroke:grey;stroke-width:2" />
    
                 <line x1="270" y1="255" x2="270" y2="105" style="stroke:grey;stroke-width:2" />
    
                 <line x1="850" y1="180" x2="420" y2="180" style="stroke:grey;stroke-width:2" />
                 <line x1="890" y1="180" x2="985" y2="180" style="stroke:grey;stroke-width:2" />
                 <line x1="985" y1="180" x2="985" y2="210" style="stroke:grey;stroke-width:2" />   
    
    
                 <line x1="560" y1="180" x2="560" y2="242" style="stroke:grey;stroke-width:2" />   
                 <line x1="660" y1="180" x2="660" y2="242" style="stroke:grey;stroke-width:2" />   
                 <line x1="760" y1="180" x2="760" y2="242" style="stroke:grey;stroke-width:2" />   
    
    
              <line x1="169" y1="100" x2="169" y2="130" style="stroke:grey;stroke-width:2" />
              <line x1="53" y1="100" x2="169" y2="100" style="stroke:grey;stroke-width:2" />
    
              <line x1="220" y1="110" x2="220" y2="140" style="stroke:grey;stroke-width:2;stroke-dasharray: 1, 4" />
    
             <line x1="1020" y1="160" x2="1020" y2="220" style="stroke:grey;stroke-width:2;stroke-dasharray: 1, 4" />
    
             <line x1="1035" y1="270" x2="1075" y2="270" style="stroke:grey;stroke-width:2" />
    
             <line x1="1075" y1="270" x2="1075" y2="320" style="stroke:grey;stroke-width:2" />
    
              <line x1="1075" y1="220" x2="1075" y2="320" style="stroke:grey;stroke-width:2" />
    
              <line x1="1075" y1="220" x2="1120" y2="220" style="stroke:grey;stroke-width:2" />
    
              <line x1="1075" y1="320" x2="1120" y2="320" style="stroke:grey;stroke-width:2" />
    
              <line x1="1186" y1="220" x2="1230" y2="220" style="stroke:grey;stroke-width:2" />
    
              <line x1="1186" y1="320" x2="1230" y2="320" style="stroke:grey;stroke-width:2" />
    
             <line x1="1230" y1="220" x2="1230" y2="320" style="stroke:grey;stroke-width:2" />
    
             <line x1="1230" y1="270" x2="1350" y2="270" style="stroke:grey;stroke-width:2" />
    
             <line x1="1350" y1="240" x2="1350" y2="270" style="stroke:grey;stroke-width:2" />
    
             <line x1="1350" y1="155" x2="1350" y2="190" style="stroke:grey;stroke-width:2" />  
    
             <line x1="1349" y1="155" x2="1445" y2="155" style="stroke:grey;stroke-width:2" />
    
             <line x1="1445" y1="155" x2="1445" y2="190" style="stroke:grey;stroke-width:2" />
    
             <line x1="1495" y1="250" x2="1550" y2="250" style="stroke:grey;stroke-width:2" />
    
             <line x1="1550" y1="200" x2="1550" y2="300" style="stroke:grey;stroke-width:2" />
    
             <line x1="1550" y1="200" x2="1610" y2="200" style="stroke:grey;stroke-width:2" />
    
             <line x1="1550" y1="300" x2="1610" y2="300" style="stroke:grey;stroke-width:2" />
    
             <line x1="1730" y1="300" x2="1675" y2="300" style="stroke:grey;stroke-width:2" />
    
             <line x1="1730" y1="200" x2="1675" y2="200" style="stroke:grey;stroke-width:2" />
    
             <line x1="1730" y1="200" x2="1730" y2="300" style="stroke:grey;stroke-width:2" />
    
    
             <line x1="1480" y1="200" x2="1480" y2="135" style="stroke:grey;stroke-width:2;stroke-dasharray: 1, 4" />
    
             <line x1="1730" y1="250" x2="1800" y2="250" style="stroke: grey; stroke-width: 2;" />
    
              <line x1="1800" y1="250" x2="1800" y2="530" style="stroke: grey; stroke-width: 2;" />
    
              <line x1="1770" y1="490" x2="1770" y2="530" style="stroke: grey; stroke-width: 2;" />
    
              <line x1="1690" y1="490" x2="1770" y2="490" style="stroke: grey; stroke-width: 2;" />
    
             <line x1="1730" y1="490" x2="1730" y2="610" style="stroke: grey; stroke-width: 2;" />
    
              <line x1="1610" y1="490" x2="1650" y2="490" style="stroke: grey; stroke-width: 2;" />
    
             <line x1="1610" y1="490" x2="1610" y2="530" style="stroke: grey; stroke-width: 2;" />
    
             <line x1="1500" y1="570" x2="1593" y2="570" style="stroke: grey; stroke-width: 2;" />
    
             <line x1="1500" y1="570" x2="1593" y2="570" style="stroke: grey; stroke-width: 2;" />
    
             <line x1="1500" y1="520" x2="1500" y2="620" style="stroke: grey; stroke-width: 2;" />
    
             <line x1="1500" y1="520" x2="1440" y2="520" style="stroke: grey; stroke-width: 2;" />
    
             <line x1="1500" y1="620" x2="1440" y2="620" style="stroke: grey; stroke-width: 2;" />
    
             <line x1="1375" y1="615" x2="1310" y2="615" style="stroke: grey; stroke-width: 2;" />
    
             <line x1="1375" y1="517" x2="1310" y2="517" style="stroke: grey; stroke-width: 2;" />
    
             <line x1="1310" y1="516" x2="1310" y2="615" style="stroke: grey; stroke-width: 2;" />
    
             <line x1="1220" y1="550" x2="1310" y2="550" style="stroke: grey; stroke-width: 2;" />
    
             <line x1="1220" y1="550" x2="1220" y2="590" style="stroke: grey; stroke-width: 2;" />
    
             <line x1="1250" y1="550" x2="1250" y2="643" style="stroke: grey; stroke-width: 2;" />
    
              <line x1="1224" y1="642" x2="1250" y2="642" style="stroke: grey; stroke-width: 2;" />
    
              <line x1="1224" y1="642" x2="1224" y2="662" style="stroke: grey; stroke-width: 2;" />
    
             <line x1="1085" y1="595" x2="1160" y2="595" style="stroke: grey; stroke-width: 2;" />
    
             <line x1="1085" y1="743" x2="1085" y2="595" style="stroke: grey; stroke-width: 2;" />
    
              <line x1="1085" y1="743" x2="1160" y2="743" style="stroke: grey; stroke-width: 2;"/>
    
               <line x1="1177" y1="601" x2="1177" y2="625" style="stroke: grey; stroke-width: 2;"/>
    
              <line x1="1130" y1="625" x2="1177" y2="625" style="stroke: grey; stroke-width: 2;"/>
    
              <line x1="1130" y1="625" x2="1130" y2="718" style="stroke: grey; stroke-width: 2;"/>
    
              <line x1="1130" y1="718" x2="1220" y2="718" style="stroke: grey; stroke-width: 2;"/>
    
             <line x1="1220" y1="718" x2="1220" y2="732" style="stroke: grey; stroke-width: 2;"/>
    
             <line x1="1130" y1="690" x2="1180" y2="690" style="stroke: grey; stroke-width: 2;"/>
    
             <line x1="1180" y1="670" x2="1180" y2="690" style="stroke: grey; stroke-width: 2;"/>
    
    
    
             <line x1="530" y1="665" x2="1160" y2="665" style="stroke: grey; stroke-width: 2;"/>
             
             <line x1="630" y1="530" x2="630" y2="665" style="stroke: grey; stroke-width: 2;"/>
    
             <line x1="530" y1="530" x2="630" y2="530" style="stroke: grey; stroke-width: 2;"/>
    
             <line x1="400" y1="560" x2="465" y2="560" style="stroke: grey; stroke-width: 2;"/>
             
             <line x1="400" y1="695" x2="465" y2="695" style="stroke: grey; stroke-width: 2;"/>
             
             <line x1="366" y1="470" x2="366" y2="542" style="stroke: grey; stroke-width: 2;"/>
             
             <line x1="366" y1="470" x2="1270" y2="470" style="stroke: grey; stroke-width: 2;"/>
             
             <line x1="1270" y1="470" x2="1270" y2="550" style="stroke: grey; stroke-width: 2;"/>
    
             <line x1="366" y1="671" x2="366" y2="625" style="stroke: grey; stroke-width: 2;"/>
             
             <line x1="134" y1="625" x2="366" y2="625" style="stroke: grey; stroke-width: 2;"/>
    
             <line x1="134" y1="70" x2="134" y2="625" style="stroke: grey; stroke-width: 2;"/>
             
             <line x1="134" y1="70" x2="185" y2="70" style="stroke: grey; stroke-width: 2;"/>
                
             <line x1="185" y1="70" x2="185" y2="131" style="stroke: grey; stroke-width: 2;"/>
             
             <line x1="1562" y1="570" x2="1562" y2="840" style="stroke: grey; stroke-width: 2;"/>
             
             <line x1="330" y1="840" x2="1562" y2="840" style="stroke: grey; stroke-width: 2;"/>
    
             <line x1="225" y1="870" x2="265" y2="870" style="stroke: grey; stroke-width: 2;"/>
             
              <line x1="192" y1="430" x2="192" y2="847" style="stroke: grey; stroke-width: 2;"/>
              
             <line x1="192" y1="430" x2="1255" y2="430" style="stroke: grey; stroke-width: 2;"/>
               
             <line x1="1255" y1="155" x2="1255" y2="430" style="stroke: grey; stroke-width: 2;"/>
               
             <line x1="1255" y1="155" x2="1349" y2="155" style="stroke: grey; stroke-width: 2;"/>
             
              <line x1="875" y1="665" x2="875" y2="840" style="stroke: grey; stroke-width: 2;"/>
              
               <line x1="1180" y1="743" x2="1180" y2="840" style="stroke: grey; stroke-width: 2;"/>

        </svg>
            <script>
                // Initialize variables
                var currentIndex = 0;
                var p101div  = document.getElementById('p101');
                var p102div = document.getElementById('p102');
                var mv101div =  document.getElementById('mv101');
                var lit101div =  document.getElementById('lit101');
                var mv201div =  document.getElementById('mv201');
                var lit301div =  document.getElementById('lit301');
                var p301div =  document.getElementById('p301');
                var p302div =  document.getElementById('p302');
                var mv302div =  document.getElementById('mv302');
                var p401div =  document.getElementById('p401');
                var p402div =  document.getElementById('p402');
                var lit401div =  document.getElementById('lit401');
                var p501div =  document.getElementById('p501');
                var p502div =  document.getElementById('p502');                
                
                // Function to display the next row
                function displayNextRow() {
                    var p101arr = <?php echo json_encode($P101); ?>;
                    var p102arr = <?php echo json_encode($P102); ?>;
                    var mv101arr = <?php echo json_encode($MV101); ?>;
                    var lit101arr = <?php echo json_encode($P102); ?>;
                    var mv201arr = <?php echo json_encode($MV201); ?>;
                    var lit301arr = <?php echo json_encode($LIT301); ?>;
                    var p301arr = <?php echo json_encode($P301); ?>;
                    var p302arr = <?php echo json_encode($P302); ?>;
                    var mv302arr = <?php echo json_encode($MV302); ?>;
                    var p401arr = <?php echo json_encode($P401); ?>;
                    var p402arr = <?php echo json_encode($P402); ?>;
                    var lit401arr = <?php echo json_encode($LIT401); ?>;
                    var p501arr = <?php echo json_encode($P501); ?>;
                    var p502arr = <?php echo json_encode($P502); ?>;
                    
                    
                    if (currentIndex < p101arr.length) {
                    
                        p101div.innerText = p101arr[currentIndex];
                        p102div.innerText = p102arr[currentIndex];
                        mv101div.innerText = mv101arr[currentIndex];
                        lit101div.innerText = lit101arr[currentIndex];
                        mv201div.innerText = mv201arr[currentIndex];
                        lit301div.innerText = lit301arr[currentIndex];
                        p301div.innerText = p301arr[currentIndex];
                        p302div.innerText = p302arr[currentIndex];
                        mv302div.innerText = mv302arr[currentIndex];
                        p401div.innerText = p401arr[currentIndex];
                        p402div.innerText = p402arr[currentIndex];
                        lit401div.innerText = lit401arr[currentIndex];
                        p501div.innerText = p501arr[currentIndex];
                        p502div.innerText = p502arr[currentIndex];
                        
                        currentIndex++;
                        setTimeout(displayNextRow, 1000); // Call the function recursively after 1 second
                    } else {
                        currentIndex = 0;
                        setTimeout(displayNextRow, 1000); // Start displaying rows again from the first row after 1 second
                    }
                }
                
                // Call the displayNextRow function to start displaying rows
                displayNextRow();
            </script>
    </body>
    </html>
    """

html_file_path = 'C:/xampp/htdocs/simulation/simulation.php'
with open(html_file_path, 'w') as html_file:
    html_file.write(html_content)

print(f"HTML file saved successfully at {html_file_path}")
