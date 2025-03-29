let canvas = document.getElementById('canvas');
let ctx = canvas.getContext('2d');
   // Retângulo vermelho
        ctx.beginPath();
        ctx.lineWidth = 2;
        ctx.fillStyle = 'blue';
        ctx.strokeStyle = 'blue';
        ctx.fillRect(0, 0, 80, 70);
        ctx.strokeRect(0, 0, 80, 70);
        ctx.closePath();

        // Retângulo amarelo
        ctx.beginPath();
        ctx.lineWidth = 2;
        ctx.fillStyle = 'yellow';
        ctx.strokeStyle = 'black'; 
        ctx.fillRect(0, 300, 100, 100);
        ctx.stroke();
        ctx.closePath();
        //branco no amarelo
        ctx.beginPath();
        ctx.lineWidth = 2;
        ctx.fillStyle = 'white';
        ctx.strokeStyle = 'black'; 
        ctx.fillRect(50, 300, 50, 50);
        ctx.stroke();
        ctx.closePath();    
        
        // Retângulo azul
        ctx.beginPath();
        ctx.lineWidth = 2;
        ctx.fillStyle = 'red';
        ctx.strokeStyle = 'red';
        ctx.fillRect(320, 0, 90, 70);
        ctx.stroke();
        ctx.closePath();
        // Retângulo preto
        ctx.beginPath();
        ctx.lineWidth = 2;
        ctx.fillStyle = 'black';
        ctx.strokeStyle = 'black'; 
        ctx.fillRect(300, 300, 100, 100);
        ctx.stroke();
         //branco no amarelo
         ctx.beginPath();
         ctx.lineWidth = 2;
         ctx.fillStyle = 'white';
         ctx.strokeStyle = 'black'; 
         ctx.fillRect(300, 300, 50, 50);
         ctx.stroke();
         ctx.closePath();
         //texto
        ctx.beginPath();
        ctx.lineWidth = 2;
        ctx.fillStyle = 'black';
        ctx.font = "20px Arial";
        ctx.texAlign = "center";
        ctx.fillText("Canvas",160,45);
        ctx.closePath();
        //linha azul
        ctx.beginPath();              
        ctx.moveTo(50, 50);            
        ctx.lineTo(200,200);          
        ctx.lineWidth = 2;            
        ctx.strokeStyle = 'blue';      
        ctx.stroke();                  
        ctx.closePath();     
        //linha red
        ctx.beginPath();              
        ctx.moveTo(340, 50);            
        ctx.lineTo(200,200);          
        ctx.lineWidth = 2;            
        ctx.strokeStyle = 'red';      
        ctx.stroke();                  
        ctx.closePath();     
        //linha meio horizontal
        ctx.beginPath();              
        ctx.moveTo(0, 200);            
        ctx.lineTo(500,200);          
        ctx.lineWidth = 2;            
        ctx.strokeStyle = 'green';      
        ctx.stroke();                  
        ctx.closePath();
        //linha meio vertical
        ctx.beginPath();              
        ctx.moveTo(200,350);            
        ctx.lineTo(200,200);          
        ctx.lineWidth = 2;            
        ctx.strokeStyle = 'blue';      
        ctx.stroke();                  
        ctx.closePath();        
        //arco meio completo
        ctx.beginPath();
        ctx.arc(200,200, 80, Math.PI, 0, false); 
        ctx.lineWidth = 2;      
        ctx.strokeStyle = 'green';  
        ctx.stroke();           
        ctx.closePath();         
        //arco meio incompleto
        ctx.beginPath();
        ctx.arc(200,200,100,Math.PI,-2.36); 
        ctx.lineWidth = 2;     
        ctx.strokeStyle = 'green';  
        ctx.stroke();           
        ctx.closePath();    
        //arco meio incompleto direita
        //arco meio incompleto
        ctx.beginPath();
        ctx.arc(200,200,100,-Math.PI/ 3.8,Math.PI/ 200); 
        ctx.lineWidth = 2;     
        ctx.strokeStyle = 'green';  
        ctx.stroke();           
        ctx.closePath();
        //circulo meio superior
        ctx.beginPath();
        ctx.arc(200, 150, 25, 0, 2 * Math.PI); 
        ctx.fillStyle = 'aqua'; 
        ctx.fill(); 
        ctx.lineWidth = 2; 
        ctx.strokeStyle = 'black'; 
        ctx.stroke(); 
        ctx.closePath();
        //circulo esquerdo
        ctx.beginPath();
        ctx.arc(100, 300, 25, 0, 9 * Math.PI); 
        ctx.fillStyle = 'yellow'; 
        ctx.fill(); 
        ctx.lineWidth = 2; 
        ctx.strokeStyle = 'green'; 
        ctx.stroke(); 
        ctx.closePath();
        //circulo direito
        ctx.beginPath();
        ctx.arc(300, 300, 25, 0, 9 * Math.PI); 
        ctx.fillStyle = 'yellow'; 
        ctx.fill(); 
        ctx.lineWidth = 2; 
        ctx.strokeStyle = 'green'; 
        ctx.stroke(); 
        ctx.closePath();
        //circulo esquerdo
        ctx.beginPath();
        ctx.arc(100, 300, 25, 0, 9 * Math.PI); 
        ctx.fillStyle = 'yellow'; 
        ctx.fill(); 
        ctx.lineWidth = 2; 
        ctx.strokeStyle = 'green'; 
        ctx.stroke(); 
        ctx.closePath();

        //arco inferior incompleto esquerdo
        ctx.beginPath();
        ctx.arc(320,400,200,Math.PI,-2.22); 
        ctx.lineWidth = 2;     
        ctx.strokeStyle = 'green';  
        ctx.stroke();           
        ctx.closePath();    
        //arco inferior incompleto direito
        ctx.beginPath();
        ctx.arc(220,400,80, -2,0 * Math.PI); 
        ctx.lineWidth = 2;     
        ctx.strokeStyle = 'green';  
        ctx.stroke();           
        ctx.closePath();    