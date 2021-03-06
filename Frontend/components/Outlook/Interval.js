import React, { useState, useEffect, useRef } from 'react';


function Interval(callback, delay){
    const savedCallback = useRef();

    //remember last callback
    useEffect(() => {
        savedCallback.current = callback;
    },
     [callback]);

     //set up interval
     useEffect(() => {
         function tick() {
             savedCallback.current();
         }
         if ( delay !== null ) {
             let id = setInterval(tick, delay);
             return () => clearInterval(id);
         }
     }, [delay]);
     
}

export default Interval;