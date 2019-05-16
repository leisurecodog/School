INCLUDE Irvine32.inc
.386
.model flat,stdcall
.stack 4096
ExitProcess PROTO,dwExitCode:DWORD

; 程式說明:
; 使用 LoopTemp 變數暫存L1的counter  , OurCount儲存L2的counter且每次L2執行完都讓OurCount+1
; 每次L1開始時需把ecx儲存下來 , 再讓L2需要跑多少次的值移動到ecx給L2做迴圈執行
; L2中就只是印星號 , L2結束後會回復L1所需的counter值給ecx,並換行
.data
LoopTemp DWORD ?			;store the value of counter of loop L1
OurCount DWORD 1			;store the value of counter of loop L2
star BYTE "*",0
.code
main PROC
	mov ecx,4				;move times of L1
	mov edx,offset star		;move the address of star to edx 
L1:
	mov LoopTemp , ecx		;store ecx for L1 
	mov ecx , OurCount		;move OurCount to ecx for L2 that can run proper times
L2:
	call WriteString		;Write the String star
loop L2						;back to L2 if ecx equal zero

	inc OurCount			;make the L2 can run 1,2,3,and 4 times, so need +1 to OurCount
	call Crlf				;new line
	mov ecx , LoopTemp		;back the value of L1 to ecx
loop L1						;back to L1 if ecx equal zero
INVOKE ExitProcess,0
main ENDP
END main