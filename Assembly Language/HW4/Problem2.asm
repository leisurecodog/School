INCLUDE Irvine32.inc
.386
.model flat,stdcall
.stack 4096
ExitProcess PROTO,dwExitCode:DWORD

; �{������:
; �ϥ� LoopTemp �ܼƼȦsL1��counter  , OurCount�x�sL2��counter�B�C��L2���槹����OurCount+1
; �C��L1�}�l�ɻݧ�ecx�x�s�U�� , �A��L2�ݭn�]�h�֦����Ȳ��ʨ�ecx��L2���j�����
; L2���N�u�O�L�P�� , L2������|�^�_L1�һݪ�counter�ȵ�ecx,�ô���
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