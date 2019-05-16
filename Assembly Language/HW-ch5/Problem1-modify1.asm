INCLUDE Irvine32.inc
; Reversing a String (RevStr.asm)
; This program reverses a string.
.386
.model flat,stdcall
.stack 4096
ExitProcess proto,dwExitCode:dword
.data
	aName BYTE 50 DUP('?'),0  ;biggest size is 50 bytes
	nameSize DWORD ?	 ;
.code
main proc
	mov ecx , 50		;move biggest chars to ecx
	mov edx , offset aName	;move the address of aName to edx
	call ReadString	
	call StrLength	;eax=length of edx
	mov nameSize , eax	;move eax to nameSize
	mov ecx , nameSize	;move nameSize to ecx(counter)
	mov esi , 0		;move 0 to esi
L1:
	movzx eax , aName[esi] ;	move each aName char to eax
	push eax		;push eax to top of stack
	inc esi			;increase esi
	loop L1

	mov ecx , nameSize ;move nameSize to ecx(counter)
	mov esi , 0	;move 0 to esi
L2:
	pop eax	;pop the top of stack to eax
	mov aName[esi] , al	;move al to aName[esi]
	inc esi		;increase esi
	loop L2
	mov edx , offset aName ;move the address of aName to edx
	call WriteString	;writestring
	Invoke ExitProcess,0
	main endp
end main
