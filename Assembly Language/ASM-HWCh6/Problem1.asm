INCLUDE Irvine32.inc

.386
.model flat,stdcall
.stack 4096
ExitProcess proto,dwExitCode:dword

.data
ChooseL BYTE "EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEDDDDDDDDDDCCCCCCCCCCBBBBBBBBBBAAAAAAAAAAA",0
ErrL BYTE "Error input.",0
.code

Cla PROC
	mov esi , eax
	mov al , ChooseL[esi]
	call WriteChar
	ret
Cla ENDP

main proc
	Call ReadInt ;	Read score
Test1:
	cmp eax , 100 ;if>100 show error msg
	jg Err
	jmp Test2  ;check whether < 0
Test2:
	cmp eax , 0 ;if < 0 show error msg
	jl Err
	pushad  ;save all reg
	call Cla ;call procedure
	popad	;restore all reg
	jmp next 

Err:
	mov edx , offset ErrL
	call WriteString
	call Crlf
	jmp Next
Next:
	exit
	main endp
end main