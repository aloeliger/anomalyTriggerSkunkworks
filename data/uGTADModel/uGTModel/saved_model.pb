φΌ
Β₯
D
AddV2
x"T
y"T
z"T"
Ttype:
2	
^
AssignVariableOp
resource
value"dtype"
dtypetype"
validate_shapebool( 
~
BiasAdd

value"T	
bias"T
output"T" 
Ttype:
2	"-
data_formatstringNHWC:
NHWCNCHW
N
Cast	
x"SrcT	
y"DstT"
SrcTtype"
DstTtype"
Truncatebool( 
8
Const
output"dtype"
valuetensor"
dtypetype
^
Fill
dims"
index_type

value"T
output"T"	
Ttype"

index_typetype0:
2	
.
Identity

input"T
output"T"	
Ttype
?
	LessEqual
x"T
y"T
z
"
Ttype:
2	
q
MatMul
a"T
b"T
product"T"
transpose_abool( "
transpose_bbool( "
Ttype:

2	
>
Maximum
x"T
y"T
z"T"
Ttype:
2	

MergeV2Checkpoints
checkpoint_prefixes
destination_prefix"
delete_old_dirsbool("
allow_missing_filesbool( 
>
Minimum
x"T
y"T
z"T"
Ttype:
2	
?
Mul
x"T
y"T
z"T"
Ttype:
2	
0
Neg
x"T
y"T"
Ttype:
2
	

NoOp
M
Pack
values"T*N
output"T"
Nint(0"	
Ttype"
axisint 
C
Placeholder
output"dtype"
dtypetype"
shapeshape:
8
Pow
x"T
y"T
z"T"
Ttype:
2
	
@
ReadVariableOp
resource
value"dtype"
dtypetype
@
RealDiv
x"T
y"T
z"T"
Ttype:
2	
E
Relu
features"T
activations"T"
Ttype:
2	
o
	RestoreV2

prefix
tensor_names
shape_and_slices
tensors2dtypes"
dtypes
list(type)(0
2
Round
x"T
y"T"
Ttype:
2
	
l
SaveV2

prefix
tensor_names
shape_and_slices
tensors2dtypes"
dtypes
list(type)(0
?
Select
	condition

t"T
e"T
output"T"	
Ttype
A
SelectV2
	condition

t"T
e"T
output"T"	
Ttype
P
Shape

input"T
output"out_type"	
Ttype"
out_typetype0:
2	
H
ShardedFilename
basename	
shard

num_shards
filename
Α
StatefulPartitionedCall
args2Tin
output2Tout"
Tin
list(type)("
Tout
list(type)("	
ffunc"
configstring "
config_protostring "
executor_typestring ¨
@
StaticRegexFullMatch	
input

output
"
patternstring
2
StopGradient

input"T
output"T"	
Ttype
N

StringJoin
inputs*N

output"
Nint(0"
	separatorstring 
<
Sub
x"T
y"T
z"T"
Ttype:
2	

VarHandleOp
resource"
	containerstring "
shared_namestring "
dtypetype"
shapeshape"#
allowed_deviceslist(string)
 "serve*2.10.02unknown8«’
f
mu/biasVarHandleOp*
_output_shapes
: *
dtype0*
shape:*
shared_name	mu/bias
_
mu/bias/Read/ReadVariableOpReadVariableOpmu/bias*
_output_shapes
:*
dtype0
n
	mu/kernelVarHandleOp*
_output_shapes
: *
dtype0*
shape
:*
shared_name	mu/kernel
g
mu/kernel/Read/ReadVariableOpReadVariableOp	mu/kernel*
_output_shapes

:*
dtype0
t
q_dense_1/biasVarHandleOp*
_output_shapes
: *
dtype0*
shape:*
shared_nameq_dense_1/bias
m
"q_dense_1/bias/Read/ReadVariableOpReadVariableOpq_dense_1/bias*
_output_shapes
:*
dtype0
|
q_dense_1/kernelVarHandleOp*
_output_shapes
: *
dtype0*
shape
: *!
shared_nameq_dense_1/kernel
u
$q_dense_1/kernel/Read/ReadVariableOpReadVariableOpq_dense_1/kernel*
_output_shapes

: *
dtype0
p
q_dense/biasVarHandleOp*
_output_shapes
: *
dtype0*
shape: *
shared_nameq_dense/bias
i
 q_dense/bias/Read/ReadVariableOpReadVariableOpq_dense/bias*
_output_shapes
: *
dtype0
x
q_dense/kernelVarHandleOp*
_output_shapes
: *
dtype0*
shape
:9 *
shared_nameq_dense/kernel
q
"q_dense/kernel/Read/ReadVariableOpReadVariableOpq_dense/kernel*
_output_shapes

:9 *
dtype0
z
serving_default_input_1Placeholder*'
_output_shapes
:?????????9*
dtype0*
shape:?????????9

StatefulPartitionedCallStatefulPartitionedCallserving_default_input_1q_dense/kernelq_dense/biasq_dense_1/kernelq_dense_1/bias	mu/kernelmu/bias*
Tin
	2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*(
_read_only_resource_inputs

*-
config_proto

CPU

GPU 2J 8 *+
f&R$
"__inference_signature_wrapper_1408

NoOpNoOp
θ"
ConstConst"/device:CPU:0*
_output_shapes
: *
dtype0*£"
value"B" B"
Μ
layer-0
layer-1
layer_with_weights-0
layer-2
layer_with_weights-1
layer-3
layer_with_weights-2
layer-4
	variables
trainable_variables
regularization_losses
		keras_api

__call__
*&call_and_return_all_conditional_losses
_default_save_signature

signatures*
* 

	variables
trainable_variables
regularization_losses
	keras_api
__call__
*&call_and_return_all_conditional_losses
	quantizer* 
¬
	variables
trainable_variables
regularization_losses
	keras_api
__call__
*&call_and_return_all_conditional_losses
kernel_quantizer
bias_quantizer
kernel_quantizer_internal
bias_quantizer_internal

quantizers

activation

 kernel
!bias*
¬
"	variables
#trainable_variables
$regularization_losses
%	keras_api
&__call__
*'&call_and_return_all_conditional_losses
(kernel_quantizer
)bias_quantizer
(kernel_quantizer_internal
*bias_quantizer_internal
+
quantizers
,
activation

-kernel
.bias*
¬
/	variables
0trainable_variables
1regularization_losses
2	keras_api
3__call__
*4&call_and_return_all_conditional_losses
5kernel_quantizer
6bias_quantizer
7kernel_quantizer_internal
8bias_quantizer_internal
9
quantizers
:
activation

;kernel
<bias*
.
 0
!1
-2
.3
;4
<5*
.
 0
!1
-2
.3
;4
<5*

=0
>1* 
°
?non_trainable_variables

@layers
Ametrics
Blayer_regularization_losses
Clayer_metrics
	variables
trainable_variables
regularization_losses

__call__
_default_save_signature
*&call_and_return_all_conditional_losses
&"call_and_return_conditional_losses*
6
Dtrace_0
Etrace_1
Ftrace_2
Gtrace_3* 
6
Htrace_0
Itrace_1
Jtrace_2
Ktrace_3* 
* 

Lserving_default* 
* 
* 
* 

Mnon_trainable_variables

Nlayers
Ometrics
Player_regularization_losses
Qlayer_metrics
	variables
trainable_variables
regularization_losses
__call__
*&call_and_return_all_conditional_losses
&"call_and_return_conditional_losses* 

Rtrace_0* 

Strace_0* 
* 

 0
!1*

 0
!1*
	
=0* 

Tnon_trainable_variables

Ulayers
Vmetrics
Wlayer_regularization_losses
Xlayer_metrics
	variables
trainable_variables
regularization_losses
__call__
*&call_and_return_all_conditional_losses
&"call_and_return_conditional_losses*

Ytrace_0* 

Ztrace_0* 
* 


[config* 
* 

0
1* 
* 
^X
VARIABLE_VALUEq_dense/kernel6layer_with_weights-0/kernel/.ATTRIBUTES/VARIABLE_VALUE*
ZT
VARIABLE_VALUEq_dense/bias4layer_with_weights-0/bias/.ATTRIBUTES/VARIABLE_VALUE*

-0
.1*

-0
.1*
	
>0* 

\non_trainable_variables

]layers
^metrics
_layer_regularization_losses
`layer_metrics
"	variables
#trainable_variables
$regularization_losses
&__call__
*'&call_and_return_all_conditional_losses
&'"call_and_return_conditional_losses*

atrace_0* 

btrace_0* 
* 


cconfig* 
* 

(0
*1* 
* 
`Z
VARIABLE_VALUEq_dense_1/kernel6layer_with_weights-1/kernel/.ATTRIBUTES/VARIABLE_VALUE*
\V
VARIABLE_VALUEq_dense_1/bias4layer_with_weights-1/bias/.ATTRIBUTES/VARIABLE_VALUE*

;0
<1*

;0
<1*
* 

dnon_trainable_variables

elayers
fmetrics
glayer_regularization_losses
hlayer_metrics
/	variables
0trainable_variables
1regularization_losses
3__call__
*4&call_and_return_all_conditional_losses
&4"call_and_return_conditional_losses*

itrace_0* 

jtrace_0* 


kconfig* 


lconfig* 
* 
* 

70
81* 
* 
YS
VARIABLE_VALUE	mu/kernel6layer_with_weights-2/kernel/.ATTRIBUTES/VARIABLE_VALUE*
UO
VARIABLE_VALUEmu/bias4layer_with_weights-2/bias/.ATTRIBUTES/VARIABLE_VALUE*

mtrace_0* 

ntrace_0* 
* 
'
0
1
2
3
4*
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
	
=0* 
* 
* 
* 
* 
* 
* 
* 
	
>0* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
* 
O
saver_filenamePlaceholder*
_output_shapes
: *
dtype0*
shape: 
λ
StatefulPartitionedCall_1StatefulPartitionedCallsaver_filename"q_dense/kernel/Read/ReadVariableOp q_dense/bias/Read/ReadVariableOp$q_dense_1/kernel/Read/ReadVariableOp"q_dense_1/bias/Read/ReadVariableOpmu/kernel/Read/ReadVariableOpmu/bias/Read/ReadVariableOpConst*
Tin

2*
Tout
2*
_collective_manager_ids
 *
_output_shapes
: * 
_read_only_resource_inputs
 *-
config_proto

CPU

GPU 2J 8 *&
f!R
__inference__traced_save_2617
ξ
StatefulPartitionedCall_2StatefulPartitionedCallsaver_filenameq_dense/kernelq_dense/biasq_dense_1/kernelq_dense_1/bias	mu/kernelmu/bias*
Tin
	2*
Tout
2*
_collective_manager_ids
 *
_output_shapes
: * 
_read_only_resource_inputs
 *-
config_proto

CPU

GPU 2J 8 *)
f$R"
 __inference__traced_restore_2645’ι
γ
ώ
$__inference_model_layer_call_fn_1194
input_1
unknown:9 
	unknown_0: 
	unknown_1: 
	unknown_2:
	unknown_3:
	unknown_4:
identity’StatefulPartitionedCall
StatefulPartitionedCallStatefulPartitionedCallinput_1unknown	unknown_0	unknown_1	unknown_2	unknown_3	unknown_4*
Tin
	2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*(
_read_only_resource_inputs

*-
config_proto

CPU

GPU 2J 8 *H
fCRA
?__inference_model_layer_call_and_return_conditional_losses_1179o
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*'
_output_shapes
:?????????`
NoOpNoOp^StatefulPartitionedCall*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*2
_input_shapes!
:?????????9: : : : : : 22
StatefulPartitionedCallStatefulPartitionedCall:P L
'
_output_shapes
:?????????9
!
_user_specified_name	input_1
ψ
ψ
__inference__traced_save_2617
file_prefix-
)savev2_q_dense_kernel_read_readvariableop+
'savev2_q_dense_bias_read_readvariableop/
+savev2_q_dense_1_kernel_read_readvariableop-
)savev2_q_dense_1_bias_read_readvariableop(
$savev2_mu_kernel_read_readvariableop&
"savev2_mu_bias_read_readvariableop
savev2_const

identity_1’MergeV2Checkpointsw
StaticRegexFullMatchStaticRegexFullMatchfile_prefix"/device:CPU:**
_output_shapes
: *
pattern
^s3://.*Z
ConstConst"/device:CPU:**
_output_shapes
: *
dtype0*
valueB B.parta
Const_1Const"/device:CPU:**
_output_shapes
: *
dtype0*
valueB B
_temp/part
SelectSelectStaticRegexFullMatch:output:0Const:output:0Const_1:output:0"/device:CPU:**
T0*
_output_shapes
: f

StringJoin
StringJoinfile_prefixSelect:output:0"/device:CPU:**
N*
_output_shapes
: L

num_shardsConst*
_output_shapes
: *
dtype0*
value	B :f
ShardedFilename/shardConst"/device:CPU:0*
_output_shapes
: *
dtype0*
value	B : 
ShardedFilenameShardedFilenameStringJoin:output:0ShardedFilename/shard:output:0num_shards:output:0"/device:CPU:0*
_output_shapes
: Τ
SaveV2/tensor_namesConst"/device:CPU:0*
_output_shapes
:*
dtype0*ύ
valueσBπB6layer_with_weights-0/kernel/.ATTRIBUTES/VARIABLE_VALUEB4layer_with_weights-0/bias/.ATTRIBUTES/VARIABLE_VALUEB6layer_with_weights-1/kernel/.ATTRIBUTES/VARIABLE_VALUEB4layer_with_weights-1/bias/.ATTRIBUTES/VARIABLE_VALUEB6layer_with_weights-2/kernel/.ATTRIBUTES/VARIABLE_VALUEB4layer_with_weights-2/bias/.ATTRIBUTES/VARIABLE_VALUEB_CHECKPOINTABLE_OBJECT_GRAPH{
SaveV2/shape_and_slicesConst"/device:CPU:0*
_output_shapes
:*
dtype0*!
valueBB B B B B B B ¬
SaveV2SaveV2ShardedFilename:filename:0SaveV2/tensor_names:output:0 SaveV2/shape_and_slices:output:0)savev2_q_dense_kernel_read_readvariableop'savev2_q_dense_bias_read_readvariableop+savev2_q_dense_1_kernel_read_readvariableop)savev2_q_dense_1_bias_read_readvariableop$savev2_mu_kernel_read_readvariableop"savev2_mu_bias_read_readvariableopsavev2_const"/device:CPU:0*
_output_shapes
 *
dtypes
	2
&MergeV2Checkpoints/checkpoint_prefixesPackShardedFilename:filename:0^SaveV2"/device:CPU:0*
N*
T0*
_output_shapes
:
MergeV2CheckpointsMergeV2Checkpoints/MergeV2Checkpoints/checkpoint_prefixes:output:0file_prefix"/device:CPU:0*
_output_shapes
 f
IdentityIdentityfile_prefix^MergeV2Checkpoints"/device:CPU:0*
T0*
_output_shapes
: Q

Identity_1IdentityIdentity:output:0^NoOp*
T0*
_output_shapes
: [
NoOpNoOp^MergeV2Checkpoints*"
_acd_function_control_output(*
_output_shapes
 "!

identity_1Identity_1:output:0*G
_input_shapes6
4: :9 : : :::: 2(
MergeV2CheckpointsMergeV2Checkpoints:C ?

_output_shapes
: 
%
_user_specified_namefile_prefix:$ 

_output_shapes

:9 : 

_output_shapes
: :$ 

_output_shapes

: : 

_output_shapes
::$ 

_output_shapes

:: 

_output_shapes
::

_output_shapes
: 
―E

<__inference_mu_layer_call_and_return_conditional_losses_2554

inputs)
readvariableop_resource:'
readvariableop_3_resource:
identity’ReadVariableOp’ReadVariableOp_1’ReadVariableOp_2’ReadVariableOp_3’ReadVariableOp_4’ReadVariableOp_5G
Pow/xConst*
_output_shapes
: *
dtype0*
value	B :G
Pow/yConst*
_output_shapes
: *
dtype0*
value	B :K
PowPowPow/x:output:0Pow/y:output:0*
T0*
_output_shapes
: E
CastCastPow:z:0*

DstT0*

SrcT0*
_output_shapes
: f
ReadVariableOpReadVariableOpreadvariableop_resource*
_output_shapes

:*
dtype0J
mul/yConst*
_output_shapes
: *
dtype0*
valueB
 *   B[
mulMulReadVariableOp:value:0mul/y:output:0*
T0*
_output_shapes

:N
truedivRealDivmul:z:0Cast:y:0*
T0*
_output_shapes

:@
NegNegtruediv:z:0*
T0*
_output_shapes

:D
RoundRoundtruediv:z:0*
T0*
_output_shapes

:I
addAddV2Neg:y:0	Round:y:0*
T0*
_output_shapes

:N
StopGradientStopGradientadd:z:0*
T0*
_output_shapes

:[
add_1AddV2truediv:z:0StopGradient:output:0*
T0*
_output_shapes

:\
clip_by_value/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 *  ψAv
clip_by_value/MinimumMinimum	add_1:z:0 clip_by_value/Minimum/y:output:0*
T0*
_output_shapes

:T
clip_by_value/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Βv
clip_by_valueMaximumclip_by_value/Minimum:z:0clip_by_value/y:output:0*
T0*
_output_shapes

:R
mul_1MulCast:y:0clip_by_value:z:0*
T0*
_output_shapes

:P
truediv_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   B^
	truediv_1RealDiv	mul_1:z:0truediv_1/y:output:0*
T0*
_output_shapes

:L
mul_2/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?V
mul_2Mulmul_2/x:output:0truediv_1:z:0*
T0*
_output_shapes

:h
ReadVariableOp_1ReadVariableOpreadvariableop_resource*
_output_shapes

:*
dtype0O
Neg_1NegReadVariableOp_1:value:0*
T0*
_output_shapes

:M
add_2AddV2	Neg_1:y:0	mul_2:z:0*
T0*
_output_shapes

:L
mul_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?R
mul_3Mulmul_3/x:output:0	add_2:z:0*
T0*
_output_shapes

:R
StopGradient_1StopGradient	mul_3:z:0*
T0*
_output_shapes

:h
ReadVariableOp_2ReadVariableOpreadvariableop_resource*
_output_shapes

:*
dtype0j
add_3AddV2ReadVariableOp_2:value:0StopGradient_1:output:0*
T0*
_output_shapes

:U
MatMulMatMulinputs	add_3:z:0*
T0*'
_output_shapes
:?????????I
Pow_1/xConst*
_output_shapes
: *
dtype0*
value	B :I
Pow_1/yConst*
_output_shapes
: *
dtype0*
value	B :Q
Pow_1PowPow_1/x:output:0Pow_1/y:output:0*
T0*
_output_shapes
: I
Cast_1Cast	Pow_1:z:0*

DstT0*

SrcT0*
_output_shapes
: f
ReadVariableOp_3ReadVariableOpreadvariableop_3_resource*
_output_shapes
:*
dtype0L
mul_4/yConst*
_output_shapes
: *
dtype0*
valueB
 *   D]
mul_4MulReadVariableOp_3:value:0mul_4/y:output:0*
T0*
_output_shapes
:P
	truediv_2RealDiv	mul_4:z:0
Cast_1:y:0*
T0*
_output_shapes
:@
Neg_2Negtruediv_2:z:0*
T0*
_output_shapes
:D
Round_1Roundtruediv_2:z:0*
T0*
_output_shapes
:K
add_4AddV2	Neg_2:y:0Round_1:y:0*
T0*
_output_shapes
:N
StopGradient_2StopGradient	add_4:z:0*
T0*
_output_shapes
:[
add_5AddV2truediv_2:z:0StopGradient_2:output:0*
T0*
_output_shapes
:^
clip_by_value_1/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * ?Cv
clip_by_value_1/MinimumMinimum	add_5:z:0"clip_by_value_1/Minimum/y:output:0*
T0*
_output_shapes
:V
clip_by_value_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Δx
clip_by_value_1Maximumclip_by_value_1/Minimum:z:0clip_by_value_1/y:output:0*
T0*
_output_shapes
:R
mul_5Mul
Cast_1:y:0clip_by_value_1:z:0*
T0*
_output_shapes
:P
truediv_3/yConst*
_output_shapes
: *
dtype0*
valueB
 *   DZ
	truediv_3RealDiv	mul_5:z:0truediv_3/y:output:0*
T0*
_output_shapes
:L
mul_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?R
mul_6Mulmul_6/x:output:0truediv_3:z:0*
T0*
_output_shapes
:f
ReadVariableOp_4ReadVariableOpreadvariableop_3_resource*
_output_shapes
:*
dtype0K
Neg_3NegReadVariableOp_4:value:0*
T0*
_output_shapes
:I
add_6AddV2	Neg_3:y:0	mul_6:z:0*
T0*
_output_shapes
:L
mul_7/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?N
mul_7Mulmul_7/x:output:0	add_6:z:0*
T0*
_output_shapes
:N
StopGradient_3StopGradient	mul_7:z:0*
T0*
_output_shapes
:f
ReadVariableOp_5ReadVariableOpreadvariableop_3_resource*
_output_shapes
:*
dtype0f
add_7AddV2ReadVariableOp_5:value:0StopGradient_3:output:0*
T0*
_output_shapes
:a
BiasAddBiasAddMatMul:product:0	add_7:z:0*
T0*'
_output_shapes
:?????????I
Pow_2/xConst*
_output_shapes
: *
dtype0*
value	B :I
Pow_2/yConst*
_output_shapes
: *
dtype0*
value	B :Q
Pow_2PowPow_2/x:output:0Pow_2/y:output:0*
T0*
_output_shapes
: I
Cast_2Cast	Pow_2:z:0*

DstT0*

SrcT0*
_output_shapes
: L
mul_8/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Db
mul_8MulBiasAdd:output:0mul_8/y:output:0*
T0*'
_output_shapes
:?????????]
	truediv_4RealDiv	mul_8:z:0
Cast_2:y:0*
T0*'
_output_shapes
:?????????M
Neg_4Negtruediv_4:z:0*
T0*'
_output_shapes
:?????????Q
Round_2Roundtruediv_4:z:0*
T0*'
_output_shapes
:?????????X
add_8AddV2	Neg_4:y:0Round_2:y:0*
T0*'
_output_shapes
:?????????[
StopGradient_4StopGradient	add_8:z:0*
T0*'
_output_shapes
:?????????h
add_9AddV2truediv_4:z:0StopGradient_4:output:0*
T0*'
_output_shapes
:?????????^
clip_by_value_2/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * ?C
clip_by_value_2/MinimumMinimum	add_9:z:0"clip_by_value_2/Minimum/y:output:0*
T0*'
_output_shapes
:?????????V
clip_by_value_2/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Δ
clip_by_value_2Maximumclip_by_value_2/Minimum:z:0clip_by_value_2/y:output:0*
T0*'
_output_shapes
:?????????_
mul_9Mul
Cast_2:y:0clip_by_value_2:z:0*
T0*'
_output_shapes
:?????????P
truediv_5/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Dg
	truediv_5RealDiv	mul_9:z:0truediv_5/y:output:0*
T0*'
_output_shapes
:?????????M
mul_10/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?a
mul_10Mulmul_10/x:output:0truediv_5:z:0*
T0*'
_output_shapes
:?????????P
Neg_5NegBiasAdd:output:0*
T0*'
_output_shapes
:?????????X
add_10AddV2	Neg_5:y:0
mul_10:z:0*
T0*'
_output_shapes
:?????????M
mul_11/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?^
mul_11Mulmul_11/x:output:0
add_10:z:0*
T0*'
_output_shapes
:?????????\
StopGradient_5StopGradient
mul_11:z:0*
T0*'
_output_shapes
:?????????l
add_11AddV2BiasAdd:output:0StopGradient_5:output:0*
T0*'
_output_shapes
:?????????Y
IdentityIdentity
add_11:z:0^NoOp*
T0*'
_output_shapes
:?????????Ά
NoOpNoOp^ReadVariableOp^ReadVariableOp_1^ReadVariableOp_2^ReadVariableOp_3^ReadVariableOp_4^ReadVariableOp_5*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime**
_input_shapes
:?????????: : 2 
ReadVariableOpReadVariableOp2$
ReadVariableOp_1ReadVariableOp_12$
ReadVariableOp_2ReadVariableOp_22$
ReadVariableOp_3ReadVariableOp_32$
ReadVariableOp_4ReadVariableOp_42$
ReadVariableOp_5ReadVariableOp_5:O K
'
_output_shapes
:?????????
 
_user_specified_nameinputs
»

&__inference_q_dense_layer_call_fn_2203

inputs
unknown:9 
	unknown_0: 
identity’StatefulPartitionedCallΥ
StatefulPartitionedCallStatefulPartitionedCallinputsunknown	unknown_0*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:????????? *$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8 *I
fDRB
@__inference_q_dense_layer_call_and_return_conditional_losses_934o
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*'
_output_shapes
:????????? `
NoOpNoOp^StatefulPartitionedCall*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime**
_input_shapes
:?????????9: : 22
StatefulPartitionedCallStatefulPartitionedCall:O K
'
_output_shapes
:?????????9
 
_user_specified_nameinputs
Ο
b
F__inference_q_activation_layer_call_and_return_conditional_losses_2194

inputs
identityG
Pow/xConst*
_output_shapes
: *
dtype0*
value	B :G
Pow/yConst*
_output_shapes
: *
dtype0*
value	B :K
PowPowPow/x:output:0Pow/y:output:0*
T0*
_output_shapes
: E
CastCastPow:z:0*

DstT0*

SrcT0*
_output_shapes
: J
mul/yConst*
_output_shapes
: *
dtype0*
valueB
 *   DT
mulMulinputsmul/y:output:0*
T0*'
_output_shapes
:?????????9W
truedivRealDivmul:z:0Cast:y:0*
T0*'
_output_shapes
:?????????9I
NegNegtruediv:z:0*
T0*'
_output_shapes
:?????????9M
RoundRoundtruediv:z:0*
T0*'
_output_shapes
:?????????9R
addAddV2Neg:y:0	Round:y:0*
T0*'
_output_shapes
:?????????9W
StopGradientStopGradientadd:z:0*
T0*'
_output_shapes
:?????????9d
add_1AddV2truediv:z:0StopGradient:output:0*
T0*'
_output_shapes
:?????????9\
clip_by_value/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * ?C
clip_by_value/MinimumMinimum	add_1:z:0 clip_by_value/Minimum/y:output:0*
T0*'
_output_shapes
:?????????9T
clip_by_value/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Δ
clip_by_valueMaximumclip_by_value/Minimum:z:0clip_by_value/y:output:0*
T0*'
_output_shapes
:?????????9[
mul_1MulCast:y:0clip_by_value:z:0*
T0*'
_output_shapes
:?????????9P
truediv_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Dg
	truediv_1RealDiv	mul_1:z:0truediv_1/y:output:0*
T0*'
_output_shapes
:?????????9L
mul_2/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?_
mul_2Mulmul_2/x:output:0truediv_1:z:0*
T0*'
_output_shapes
:?????????9F
Neg_1Neginputs*
T0*'
_output_shapes
:?????????9V
add_2AddV2	Neg_1:y:0	mul_2:z:0*
T0*'
_output_shapes
:?????????9L
mul_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?[
mul_3Mulmul_3/x:output:0	add_2:z:0*
T0*'
_output_shapes
:?????????9[
StopGradient_1StopGradient	mul_3:z:0*
T0*'
_output_shapes
:?????????9a
add_3AddV2inputsStopGradient_1:output:0*
T0*'
_output_shapes
:?????????9Q
IdentityIdentity	add_3:z:0*
T0*'
_output_shapes
:?????????9"
identityIdentity:output:0*(
_construction_contextkEagerRuntime*&
_input_shapes
:?????????9:O K
'
_output_shapes
:?????????9
 
_user_specified_nameinputs

§
__inference_loss_fn_0_2565H
6q_dense_kernel_regularizer_abs_readvariableop_resource:9 
identity’-q_dense/kernel/Regularizer/Abs/ReadVariableOp€
-q_dense/kernel/Regularizer/Abs/ReadVariableOpReadVariableOp6q_dense_kernel_regularizer_abs_readvariableop_resource*
_output_shapes

:9 *
dtype0
q_dense/kernel/Regularizer/AbsAbs5q_dense/kernel/Regularizer/Abs/ReadVariableOp:value:0*
T0*
_output_shapes

:9 q
 q_dense/kernel/Regularizer/ConstConst*
_output_shapes
:*
dtype0*
valueB"       
q_dense/kernel/Regularizer/SumSum"q_dense/kernel/Regularizer/Abs:y:0)q_dense/kernel/Regularizer/Const:output:0*
T0*
_output_shapes
: e
 q_dense/kernel/Regularizer/mul/xConst*
_output_shapes
: *
dtype0*
valueB
 *o:
q_dense/kernel/Regularizer/mulMul)q_dense/kernel/Regularizer/mul/x:output:0'q_dense/kernel/Regularizer/Sum:output:0*
T0*
_output_shapes
: `
IdentityIdentity"q_dense/kernel/Regularizer/mul:z:0^NoOp*
T0*
_output_shapes
: v
NoOpNoOp.^q_dense/kernel/Regularizer/Abs/ReadVariableOp*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*
_input_shapes
: 2^
-q_dense/kernel/Regularizer/Abs/ReadVariableOp-q_dense/kernel/Regularizer/Abs/ReadVariableOp
Β#
?
?__inference_model_layer_call_and_return_conditional_losses_1377
input_1
q_dense_1349:9 
q_dense_1351:  
q_dense_1_1354: 
q_dense_1_1356:
mu_1359:
mu_1361:
identity’mu/StatefulPartitionedCall’q_dense/StatefulPartitionedCall’-q_dense/kernel/Regularizer/Abs/ReadVariableOp’!q_dense_1/StatefulPartitionedCall’/q_dense_1/kernel/Regularizer/Abs/ReadVariableOpΎ
q_activation/PartitionedCallPartitionedCallinput_1*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????9* 
_read_only_resource_inputs
 *-
config_proto

CPU

GPU 2J 8 *N
fIRG
E__inference_q_activation_layer_call_and_return_conditional_losses_813
q_dense/StatefulPartitionedCallStatefulPartitionedCall%q_activation/PartitionedCall:output:0q_dense_1349q_dense_1351*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:????????? *$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8 *I
fDRB
@__inference_q_dense_layer_call_and_return_conditional_losses_934
!q_dense_1/StatefulPartitionedCallStatefulPartitionedCall(q_dense/StatefulPartitionedCall:output:0q_dense_1_1354q_dense_1_1356*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8 *L
fGRE
C__inference_q_dense_1_layer_call_and_return_conditional_losses_1059φ
mu/StatefulPartitionedCallStatefulPartitionedCall*q_dense_1/StatefulPartitionedCall:output:0mu_1359mu_1361*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8 *E
f@R>
<__inference_mu_layer_call_and_return_conditional_losses_1160z
-q_dense/kernel/Regularizer/Abs/ReadVariableOpReadVariableOpq_dense_1349*
_output_shapes

:9 *
dtype0
q_dense/kernel/Regularizer/AbsAbs5q_dense/kernel/Regularizer/Abs/ReadVariableOp:value:0*
T0*
_output_shapes

:9 q
 q_dense/kernel/Regularizer/ConstConst*
_output_shapes
:*
dtype0*
valueB"       
q_dense/kernel/Regularizer/SumSum"q_dense/kernel/Regularizer/Abs:y:0)q_dense/kernel/Regularizer/Const:output:0*
T0*
_output_shapes
: e
 q_dense/kernel/Regularizer/mul/xConst*
_output_shapes
: *
dtype0*
valueB
 *o:
q_dense/kernel/Regularizer/mulMul)q_dense/kernel/Regularizer/mul/x:output:0'q_dense/kernel/Regularizer/Sum:output:0*
T0*
_output_shapes
: ~
/q_dense_1/kernel/Regularizer/Abs/ReadVariableOpReadVariableOpq_dense_1_1354*
_output_shapes

: *
dtype0
 q_dense_1/kernel/Regularizer/AbsAbs7q_dense_1/kernel/Regularizer/Abs/ReadVariableOp:value:0*
T0*
_output_shapes

: s
"q_dense_1/kernel/Regularizer/ConstConst*
_output_shapes
:*
dtype0*
valueB"       
 q_dense_1/kernel/Regularizer/SumSum$q_dense_1/kernel/Regularizer/Abs:y:0+q_dense_1/kernel/Regularizer/Const:output:0*
T0*
_output_shapes
: g
"q_dense_1/kernel/Regularizer/mul/xConst*
_output_shapes
: *
dtype0*
valueB
 *     
 q_dense_1/kernel/Regularizer/mulMul+q_dense_1/kernel/Regularizer/mul/x:output:0)q_dense_1/kernel/Regularizer/Sum:output:0*
T0*
_output_shapes
: r
IdentityIdentity#mu/StatefulPartitionedCall:output:0^NoOp*
T0*'
_output_shapes
:?????????
NoOpNoOp^mu/StatefulPartitionedCall ^q_dense/StatefulPartitionedCall.^q_dense/kernel/Regularizer/Abs/ReadVariableOp"^q_dense_1/StatefulPartitionedCall0^q_dense_1/kernel/Regularizer/Abs/ReadVariableOp*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*2
_input_shapes!
:?????????9: : : : : : 28
mu/StatefulPartitionedCallmu/StatefulPartitionedCall2B
q_dense/StatefulPartitionedCallq_dense/StatefulPartitionedCall2^
-q_dense/kernel/Regularizer/Abs/ReadVariableOp-q_dense/kernel/Regularizer/Abs/ReadVariableOp2F
!q_dense_1/StatefulPartitionedCall!q_dense_1/StatefulPartitionedCall2b
/q_dense_1/kernel/Regularizer/Abs/ReadVariableOp/q_dense_1/kernel/Regularizer/Abs/ReadVariableOp:P L
'
_output_shapes
:?????????9
!
_user_specified_name	input_1
Ί#
Ο
?__inference_model_layer_call_and_return_conditional_losses_1179

inputs
q_dense_935:9 
q_dense_937:  
q_dense_1_1060: 
q_dense_1_1062:
mu_1161:
mu_1163:
identity’mu/StatefulPartitionedCall’q_dense/StatefulPartitionedCall’-q_dense/kernel/Regularizer/Abs/ReadVariableOp’!q_dense_1/StatefulPartitionedCall’/q_dense_1/kernel/Regularizer/Abs/ReadVariableOp½
q_activation/PartitionedCallPartitionedCallinputs*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????9* 
_read_only_resource_inputs
 *-
config_proto

CPU

GPU 2J 8 *N
fIRG
E__inference_q_activation_layer_call_and_return_conditional_losses_813
q_dense/StatefulPartitionedCallStatefulPartitionedCall%q_activation/PartitionedCall:output:0q_dense_935q_dense_937*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:????????? *$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8 *I
fDRB
@__inference_q_dense_layer_call_and_return_conditional_losses_934
!q_dense_1/StatefulPartitionedCallStatefulPartitionedCall(q_dense/StatefulPartitionedCall:output:0q_dense_1_1060q_dense_1_1062*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8 *L
fGRE
C__inference_q_dense_1_layer_call_and_return_conditional_losses_1059φ
mu/StatefulPartitionedCallStatefulPartitionedCall*q_dense_1/StatefulPartitionedCall:output:0mu_1161mu_1163*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8 *E
f@R>
<__inference_mu_layer_call_and_return_conditional_losses_1160y
-q_dense/kernel/Regularizer/Abs/ReadVariableOpReadVariableOpq_dense_935*
_output_shapes

:9 *
dtype0
q_dense/kernel/Regularizer/AbsAbs5q_dense/kernel/Regularizer/Abs/ReadVariableOp:value:0*
T0*
_output_shapes

:9 q
 q_dense/kernel/Regularizer/ConstConst*
_output_shapes
:*
dtype0*
valueB"       
q_dense/kernel/Regularizer/SumSum"q_dense/kernel/Regularizer/Abs:y:0)q_dense/kernel/Regularizer/Const:output:0*
T0*
_output_shapes
: e
 q_dense/kernel/Regularizer/mul/xConst*
_output_shapes
: *
dtype0*
valueB
 *o:
q_dense/kernel/Regularizer/mulMul)q_dense/kernel/Regularizer/mul/x:output:0'q_dense/kernel/Regularizer/Sum:output:0*
T0*
_output_shapes
: ~
/q_dense_1/kernel/Regularizer/Abs/ReadVariableOpReadVariableOpq_dense_1_1060*
_output_shapes

: *
dtype0
 q_dense_1/kernel/Regularizer/AbsAbs7q_dense_1/kernel/Regularizer/Abs/ReadVariableOp:value:0*
T0*
_output_shapes

: s
"q_dense_1/kernel/Regularizer/ConstConst*
_output_shapes
:*
dtype0*
valueB"       
 q_dense_1/kernel/Regularizer/SumSum$q_dense_1/kernel/Regularizer/Abs:y:0+q_dense_1/kernel/Regularizer/Const:output:0*
T0*
_output_shapes
: g
"q_dense_1/kernel/Regularizer/mul/xConst*
_output_shapes
: *
dtype0*
valueB
 *     
 q_dense_1/kernel/Regularizer/mulMul+q_dense_1/kernel/Regularizer/mul/x:output:0)q_dense_1/kernel/Regularizer/Sum:output:0*
T0*
_output_shapes
: r
IdentityIdentity#mu/StatefulPartitionedCall:output:0^NoOp*
T0*'
_output_shapes
:?????????
NoOpNoOp^mu/StatefulPartitionedCall ^q_dense/StatefulPartitionedCall.^q_dense/kernel/Regularizer/Abs/ReadVariableOp"^q_dense_1/StatefulPartitionedCall0^q_dense_1/kernel/Regularizer/Abs/ReadVariableOp*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*2
_input_shapes!
:?????????9: : : : : : 28
mu/StatefulPartitionedCallmu/StatefulPartitionedCall2B
q_dense/StatefulPartitionedCallq_dense/StatefulPartitionedCall2^
-q_dense/kernel/Regularizer/Abs/ReadVariableOp-q_dense/kernel/Regularizer/Abs/ReadVariableOp2F
!q_dense_1/StatefulPartitionedCall!q_dense_1/StatefulPartitionedCall2b
/q_dense_1/kernel/Regularizer/Abs/ReadVariableOp/q_dense_1/kernel/Regularizer/Abs/ReadVariableOp:O K
'
_output_shapes
:?????????9
 
_user_specified_nameinputs
ΐ
ό
"__inference_signature_wrapper_1408
input_1
unknown:9 
	unknown_0: 
	unknown_1: 
	unknown_2:
	unknown_3:
	unknown_4:
identity’StatefulPartitionedCallθ
StatefulPartitionedCallStatefulPartitionedCallinput_1unknown	unknown_0	unknown_1	unknown_2	unknown_3	unknown_4*
Tin
	2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*(
_read_only_resource_inputs

*-
config_proto

CPU

GPU 2J 8 *'
f"R 
__inference__wrapped_model_775o
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*'
_output_shapes
:?????????`
NoOpNoOp^StatefulPartitionedCall*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*2
_input_shapes!
:?????????9: : : : : : 22
StatefulPartitionedCallStatefulPartitionedCall:P L
'
_output_shapes
:?????????9
!
_user_specified_name	input_1
χΘ
Β
__inference__wrapped_model_775
input_17
%model_q_dense_readvariableop_resource:9 5
'model_q_dense_readvariableop_3_resource: 9
'model_q_dense_1_readvariableop_resource: 7
)model_q_dense_1_readvariableop_3_resource:2
 model_mu_readvariableop_resource:0
"model_mu_readvariableop_3_resource:
identity’model/mu/ReadVariableOp’model/mu/ReadVariableOp_1’model/mu/ReadVariableOp_2’model/mu/ReadVariableOp_3’model/mu/ReadVariableOp_4’model/mu/ReadVariableOp_5’model/q_dense/ReadVariableOp’model/q_dense/ReadVariableOp_1’model/q_dense/ReadVariableOp_2’model/q_dense/ReadVariableOp_3’model/q_dense/ReadVariableOp_4’model/q_dense/ReadVariableOp_5’model/q_dense_1/ReadVariableOp’ model/q_dense_1/ReadVariableOp_1’ model/q_dense_1/ReadVariableOp_2’ model/q_dense_1/ReadVariableOp_3’ model/q_dense_1/ReadVariableOp_4’ model/q_dense_1/ReadVariableOp_5Z
model/q_activation/Pow/xConst*
_output_shapes
: *
dtype0*
value	B :Z
model/q_activation/Pow/yConst*
_output_shapes
: *
dtype0*
value	B :
model/q_activation/PowPow!model/q_activation/Pow/x:output:0!model/q_activation/Pow/y:output:0*
T0*
_output_shapes
: k
model/q_activation/CastCastmodel/q_activation/Pow:z:0*

DstT0*

SrcT0*
_output_shapes
: ]
model/q_activation/mul/yConst*
_output_shapes
: *
dtype0*
valueB
 *   D{
model/q_activation/mulMulinput_1!model/q_activation/mul/y:output:0*
T0*'
_output_shapes
:?????????9
model/q_activation/truedivRealDivmodel/q_activation/mul:z:0model/q_activation/Cast:y:0*
T0*'
_output_shapes
:?????????9o
model/q_activation/NegNegmodel/q_activation/truediv:z:0*
T0*'
_output_shapes
:?????????9s
model/q_activation/RoundRoundmodel/q_activation/truediv:z:0*
T0*'
_output_shapes
:?????????9
model/q_activation/addAddV2model/q_activation/Neg:y:0model/q_activation/Round:y:0*
T0*'
_output_shapes
:?????????9}
model/q_activation/StopGradientStopGradientmodel/q_activation/add:z:0*
T0*'
_output_shapes
:?????????9
model/q_activation/add_1AddV2model/q_activation/truediv:z:0(model/q_activation/StopGradient:output:0*
T0*'
_output_shapes
:?????????9o
*model/q_activation/clip_by_value/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * ?CΈ
(model/q_activation/clip_by_value/MinimumMinimummodel/q_activation/add_1:z:03model/q_activation/clip_by_value/Minimum/y:output:0*
T0*'
_output_shapes
:?????????9g
"model/q_activation/clip_by_value/yConst*
_output_shapes
: *
dtype0*
valueB
 *   ΔΈ
 model/q_activation/clip_by_valueMaximum,model/q_activation/clip_by_value/Minimum:z:0+model/q_activation/clip_by_value/y:output:0*
T0*'
_output_shapes
:?????????9
model/q_activation/mul_1Mulmodel/q_activation/Cast:y:0$model/q_activation/clip_by_value:z:0*
T0*'
_output_shapes
:?????????9c
model/q_activation/truediv_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   D 
model/q_activation/truediv_1RealDivmodel/q_activation/mul_1:z:0'model/q_activation/truediv_1/y:output:0*
T0*'
_output_shapes
:?????????9_
model/q_activation/mul_2/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?
model/q_activation/mul_2Mul#model/q_activation/mul_2/x:output:0 model/q_activation/truediv_1:z:0*
T0*'
_output_shapes
:?????????9Z
model/q_activation/Neg_1Neginput_1*
T0*'
_output_shapes
:?????????9
model/q_activation/add_2AddV2model/q_activation/Neg_1:y:0model/q_activation/mul_2:z:0*
T0*'
_output_shapes
:?????????9_
model/q_activation/mul_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?
model/q_activation/mul_3Mul#model/q_activation/mul_3/x:output:0model/q_activation/add_2:z:0*
T0*'
_output_shapes
:?????????9
!model/q_activation/StopGradient_1StopGradientmodel/q_activation/mul_3:z:0*
T0*'
_output_shapes
:?????????9
model/q_activation/add_3AddV2input_1*model/q_activation/StopGradient_1:output:0*
T0*'
_output_shapes
:?????????9U
model/q_dense/Pow/xConst*
_output_shapes
: *
dtype0*
value	B :U
model/q_dense/Pow/yConst*
_output_shapes
: *
dtype0*
value	B :u
model/q_dense/PowPowmodel/q_dense/Pow/x:output:0model/q_dense/Pow/y:output:0*
T0*
_output_shapes
: a
model/q_dense/CastCastmodel/q_dense/Pow:z:0*

DstT0*

SrcT0*
_output_shapes
: 
model/q_dense/ReadVariableOpReadVariableOp%model_q_dense_readvariableop_resource*
_output_shapes

:9 *
dtype0X
model/q_dense/mul/yConst*
_output_shapes
: *
dtype0*
valueB
 *   B
model/q_dense/mulMul$model/q_dense/ReadVariableOp:value:0model/q_dense/mul/y:output:0*
T0*
_output_shapes

:9 x
model/q_dense/truedivRealDivmodel/q_dense/mul:z:0model/q_dense/Cast:y:0*
T0*
_output_shapes

:9 \
model/q_dense/NegNegmodel/q_dense/truediv:z:0*
T0*
_output_shapes

:9 `
model/q_dense/RoundRoundmodel/q_dense/truediv:z:0*
T0*
_output_shapes

:9 s
model/q_dense/addAddV2model/q_dense/Neg:y:0model/q_dense/Round:y:0*
T0*
_output_shapes

:9 j
model/q_dense/StopGradientStopGradientmodel/q_dense/add:z:0*
T0*
_output_shapes

:9 
model/q_dense/add_1AddV2model/q_dense/truediv:z:0#model/q_dense/StopGradient:output:0*
T0*
_output_shapes

:9 j
%model/q_dense/clip_by_value/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 *  ψA 
#model/q_dense/clip_by_value/MinimumMinimummodel/q_dense/add_1:z:0.model/q_dense/clip_by_value/Minimum/y:output:0*
T0*
_output_shapes

:9 b
model/q_dense/clip_by_value/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Β 
model/q_dense/clip_by_valueMaximum'model/q_dense/clip_by_value/Minimum:z:0&model/q_dense/clip_by_value/y:output:0*
T0*
_output_shapes

:9 |
model/q_dense/mul_1Mulmodel/q_dense/Cast:y:0model/q_dense/clip_by_value:z:0*
T0*
_output_shapes

:9 ^
model/q_dense/truediv_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   B
model/q_dense/truediv_1RealDivmodel/q_dense/mul_1:z:0"model/q_dense/truediv_1/y:output:0*
T0*
_output_shapes

:9 Z
model/q_dense/mul_2/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?
model/q_dense/mul_2Mulmodel/q_dense/mul_2/x:output:0model/q_dense/truediv_1:z:0*
T0*
_output_shapes

:9 
model/q_dense/ReadVariableOp_1ReadVariableOp%model_q_dense_readvariableop_resource*
_output_shapes

:9 *
dtype0k
model/q_dense/Neg_1Neg&model/q_dense/ReadVariableOp_1:value:0*
T0*
_output_shapes

:9 w
model/q_dense/add_2AddV2model/q_dense/Neg_1:y:0model/q_dense/mul_2:z:0*
T0*
_output_shapes

:9 Z
model/q_dense/mul_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?|
model/q_dense/mul_3Mulmodel/q_dense/mul_3/x:output:0model/q_dense/add_2:z:0*
T0*
_output_shapes

:9 n
model/q_dense/StopGradient_1StopGradientmodel/q_dense/mul_3:z:0*
T0*
_output_shapes

:9 
model/q_dense/ReadVariableOp_2ReadVariableOp%model_q_dense_readvariableop_resource*
_output_shapes

:9 *
dtype0
model/q_dense/add_3AddV2&model/q_dense/ReadVariableOp_2:value:0%model/q_dense/StopGradient_1:output:0*
T0*
_output_shapes

:9 
model/q_dense/MatMulMatMulmodel/q_activation/add_3:z:0model/q_dense/add_3:z:0*
T0*'
_output_shapes
:????????? W
model/q_dense/Pow_1/xConst*
_output_shapes
: *
dtype0*
value	B :W
model/q_dense/Pow_1/yConst*
_output_shapes
: *
dtype0*
value	B :{
model/q_dense/Pow_1Powmodel/q_dense/Pow_1/x:output:0model/q_dense/Pow_1/y:output:0*
T0*
_output_shapes
: e
model/q_dense/Cast_1Castmodel/q_dense/Pow_1:z:0*

DstT0*

SrcT0*
_output_shapes
: 
model/q_dense/ReadVariableOp_3ReadVariableOp'model_q_dense_readvariableop_3_resource*
_output_shapes
: *
dtype0Z
model/q_dense/mul_4/yConst*
_output_shapes
: *
dtype0*
valueB
 *  E
model/q_dense/mul_4Mul&model/q_dense/ReadVariableOp_3:value:0model/q_dense/mul_4/y:output:0*
T0*
_output_shapes
: z
model/q_dense/truediv_2RealDivmodel/q_dense/mul_4:z:0model/q_dense/Cast_1:y:0*
T0*
_output_shapes
: \
model/q_dense/Neg_2Negmodel/q_dense/truediv_2:z:0*
T0*
_output_shapes
: `
model/q_dense/Round_1Roundmodel/q_dense/truediv_2:z:0*
T0*
_output_shapes
: u
model/q_dense/add_4AddV2model/q_dense/Neg_2:y:0model/q_dense/Round_1:y:0*
T0*
_output_shapes
: j
model/q_dense/StopGradient_2StopGradientmodel/q_dense/add_4:z:0*
T0*
_output_shapes
: 
model/q_dense/add_5AddV2model/q_dense/truediv_2:z:0%model/q_dense/StopGradient_2:output:0*
T0*
_output_shapes
: l
'model/q_dense/clip_by_value_1/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * πE 
%model/q_dense/clip_by_value_1/MinimumMinimummodel/q_dense/add_5:z:00model/q_dense/clip_by_value_1/Minimum/y:output:0*
T0*
_output_shapes
: d
model/q_dense/clip_by_value_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *  Ε’
model/q_dense/clip_by_value_1Maximum)model/q_dense/clip_by_value_1/Minimum:z:0(model/q_dense/clip_by_value_1/y:output:0*
T0*
_output_shapes
: |
model/q_dense/mul_5Mulmodel/q_dense/Cast_1:y:0!model/q_dense/clip_by_value_1:z:0*
T0*
_output_shapes
: ^
model/q_dense/truediv_3/yConst*
_output_shapes
: *
dtype0*
valueB
 *  E
model/q_dense/truediv_3RealDivmodel/q_dense/mul_5:z:0"model/q_dense/truediv_3/y:output:0*
T0*
_output_shapes
: Z
model/q_dense/mul_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?|
model/q_dense/mul_6Mulmodel/q_dense/mul_6/x:output:0model/q_dense/truediv_3:z:0*
T0*
_output_shapes
: 
model/q_dense/ReadVariableOp_4ReadVariableOp'model_q_dense_readvariableop_3_resource*
_output_shapes
: *
dtype0g
model/q_dense/Neg_3Neg&model/q_dense/ReadVariableOp_4:value:0*
T0*
_output_shapes
: s
model/q_dense/add_6AddV2model/q_dense/Neg_3:y:0model/q_dense/mul_6:z:0*
T0*
_output_shapes
: Z
model/q_dense/mul_7/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?x
model/q_dense/mul_7Mulmodel/q_dense/mul_7/x:output:0model/q_dense/add_6:z:0*
T0*
_output_shapes
: j
model/q_dense/StopGradient_3StopGradientmodel/q_dense/mul_7:z:0*
T0*
_output_shapes
: 
model/q_dense/ReadVariableOp_5ReadVariableOp'model_q_dense_readvariableop_3_resource*
_output_shapes
: *
dtype0
model/q_dense/add_7AddV2&model/q_dense/ReadVariableOp_5:value:0%model/q_dense/StopGradient_3:output:0*
T0*
_output_shapes
: 
model/q_dense/BiasAddBiasAddmodel/q_dense/MatMul:product:0model/q_dense/add_7:z:0*
T0*'
_output_shapes
:????????? W
model/q_dense/Pow_2/xConst*
_output_shapes
: *
dtype0*
value	B :W
model/q_dense/Pow_2/yConst*
_output_shapes
: *
dtype0*
value	B :{
model/q_dense/Pow_2Powmodel/q_dense/Pow_2/x:output:0model/q_dense/Pow_2/y:output:0*
T0*
_output_shapes
: e
model/q_dense/Cast_2Castmodel/q_dense/Pow_2:z:0*

DstT0*

SrcT0*
_output_shapes
: W
model/q_dense/Pow_3/xConst*
_output_shapes
: *
dtype0*
value	B :W
model/q_dense/Pow_3/yConst*
_output_shapes
: *
dtype0*
value	B :{
model/q_dense/Pow_3Powmodel/q_dense/Pow_3/x:output:0model/q_dense/Pow_3/y:output:0*
T0*
_output_shapes
: e
model/q_dense/Cast_3Castmodel/q_dense/Pow_3:z:0*

DstT0*

SrcT0*
_output_shapes
: X
model/q_dense/ConstConst*
_output_shapes
: *
dtype0*
valueB
 *   @X
model/q_dense/Cast_4/xConst*
_output_shapes
: *
dtype0*
value	B :m
model/q_dense/Cast_4Castmodel/q_dense/Cast_4/x:output:0*

DstT0*

SrcT0*
_output_shapes
: X
model/q_dense/sub/yConst*
_output_shapes
: *
dtype0*
valueB
 *  PAq
model/q_dense/subSubmodel/q_dense/Cast_4:y:0model/q_dense/sub/y:output:0*
T0*
_output_shapes
: p
model/q_dense/Pow_4Powmodel/q_dense/Const:output:0model/q_dense/sub:z:0*
T0*
_output_shapes
: n
model/q_dense/sub_1Submodel/q_dense/Cast_3:y:0model/q_dense/Pow_4:z:0*
T0*
_output_shapes
: 
model/q_dense/LessEqual	LessEqualmodel/q_dense/BiasAdd:output:0model/q_dense/sub_1:z:0*
T0*'
_output_shapes
:????????? l
model/q_dense/ReluRelumodel/q_dense/BiasAdd:output:0*
T0*'
_output_shapes
:????????? k
model/q_dense/ones_like/ShapeShapemodel/q_dense/BiasAdd:output:0*
T0*
_output_shapes
:b
model/q_dense/ones_like/ConstConst*
_output_shapes
: *
dtype0*
valueB
 *  ?‘
model/q_dense/ones_likeFill&model/q_dense/ones_like/Shape:output:0&model/q_dense/ones_like/Const:output:0*
T0*'
_output_shapes
:????????? n
model/q_dense/sub_2Submodel/q_dense/Cast_3:y:0model/q_dense/Pow_4:z:0*
T0*
_output_shapes
: 
model/q_dense/mul_8Mul model/q_dense/ones_like:output:0model/q_dense/sub_2:z:0*
T0*'
_output_shapes
:????????? ¬
model/q_dense/SelectV2SelectV2model/q_dense/LessEqual:z:0 model/q_dense/Relu:activations:0model/q_dense/mul_8:z:0*
T0*'
_output_shapes
:????????? 
model/q_dense/mul_9Mulmodel/q_dense/BiasAdd:output:0model/q_dense/Cast_2:y:0*
T0*'
_output_shapes
:????????? 
model/q_dense/truediv_4RealDivmodel/q_dense/mul_9:z:0model/q_dense/Cast_3:y:0*
T0*'
_output_shapes
:????????? i
model/q_dense/Neg_4Negmodel/q_dense/truediv_4:z:0*
T0*'
_output_shapes
:????????? m
model/q_dense/Round_2Roundmodel/q_dense/truediv_4:z:0*
T0*'
_output_shapes
:????????? 
model/q_dense/add_8AddV2model/q_dense/Neg_4:y:0model/q_dense/Round_2:y:0*
T0*'
_output_shapes
:????????? w
model/q_dense/StopGradient_4StopGradientmodel/q_dense/add_8:z:0*
T0*'
_output_shapes
:????????? 
model/q_dense/add_9AddV2model/q_dense/truediv_4:z:0%model/q_dense/StopGradient_4:output:0*
T0*'
_output_shapes
:????????? 
model/q_dense/truediv_5RealDivmodel/q_dense/add_9:z:0model/q_dense/Cast_2:y:0*
T0*'
_output_shapes
:????????? ^
model/q_dense/truediv_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?
model/q_dense/truediv_6RealDiv"model/q_dense/truediv_6/x:output:0model/q_dense/Cast_2:y:0*
T0*
_output_shapes
: Z
model/q_dense/sub_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?x
model/q_dense/sub_3Submodel/q_dense/sub_3/x:output:0model/q_dense/truediv_6:z:0*
T0*
_output_shapes
: 
%model/q_dense/clip_by_value_2/MinimumMinimummodel/q_dense/truediv_5:z:0model/q_dense/sub_3:z:0*
T0*'
_output_shapes
:????????? d
model/q_dense/clip_by_value_2/yConst*
_output_shapes
: *
dtype0*
valueB
 *    ―
model/q_dense/clip_by_value_2Maximum)model/q_dense/clip_by_value_2/Minimum:z:0(model/q_dense/clip_by_value_2/y:output:0*
T0*'
_output_shapes
:????????? 
model/q_dense/mul_10Mulmodel/q_dense/Cast_3:y:0!model/q_dense/clip_by_value_2:z:0*
T0*'
_output_shapes
:????????? m
model/q_dense/Neg_5Negmodel/q_dense/SelectV2:output:0*
T0*'
_output_shapes
:????????? 
model/q_dense/add_10AddV2model/q_dense/Neg_5:y:0model/q_dense/mul_10:z:0*
T0*'
_output_shapes
:????????? [
model/q_dense/mul_11/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?
model/q_dense/mul_11Mulmodel/q_dense/mul_11/x:output:0model/q_dense/add_10:z:0*
T0*'
_output_shapes
:????????? x
model/q_dense/StopGradient_5StopGradientmodel/q_dense/mul_11:z:0*
T0*'
_output_shapes
:????????? 
model/q_dense/add_11AddV2model/q_dense/SelectV2:output:0%model/q_dense/StopGradient_5:output:0*
T0*'
_output_shapes
:????????? W
model/q_dense_1/Pow/xConst*
_output_shapes
: *
dtype0*
value	B :W
model/q_dense_1/Pow/yConst*
_output_shapes
: *
dtype0*
value	B :{
model/q_dense_1/PowPowmodel/q_dense_1/Pow/x:output:0model/q_dense_1/Pow/y:output:0*
T0*
_output_shapes
: e
model/q_dense_1/CastCastmodel/q_dense_1/Pow:z:0*

DstT0*

SrcT0*
_output_shapes
: 
model/q_dense_1/ReadVariableOpReadVariableOp'model_q_dense_1_readvariableop_resource*
_output_shapes

: *
dtype0Z
model/q_dense_1/mul/yConst*
_output_shapes
: *
dtype0*
valueB
 *   B
model/q_dense_1/mulMul&model/q_dense_1/ReadVariableOp:value:0model/q_dense_1/mul/y:output:0*
T0*
_output_shapes

: ~
model/q_dense_1/truedivRealDivmodel/q_dense_1/mul:z:0model/q_dense_1/Cast:y:0*
T0*
_output_shapes

: `
model/q_dense_1/NegNegmodel/q_dense_1/truediv:z:0*
T0*
_output_shapes

: d
model/q_dense_1/RoundRoundmodel/q_dense_1/truediv:z:0*
T0*
_output_shapes

: y
model/q_dense_1/addAddV2model/q_dense_1/Neg:y:0model/q_dense_1/Round:y:0*
T0*
_output_shapes

: n
model/q_dense_1/StopGradientStopGradientmodel/q_dense_1/add:z:0*
T0*
_output_shapes

: 
model/q_dense_1/add_1AddV2model/q_dense_1/truediv:z:0%model/q_dense_1/StopGradient:output:0*
T0*
_output_shapes

: l
'model/q_dense_1/clip_by_value/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 *  ψA¦
%model/q_dense_1/clip_by_value/MinimumMinimummodel/q_dense_1/add_1:z:00model/q_dense_1/clip_by_value/Minimum/y:output:0*
T0*
_output_shapes

: d
model/q_dense_1/clip_by_value/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Β¦
model/q_dense_1/clip_by_valueMaximum)model/q_dense_1/clip_by_value/Minimum:z:0(model/q_dense_1/clip_by_value/y:output:0*
T0*
_output_shapes

: 
model/q_dense_1/mul_1Mulmodel/q_dense_1/Cast:y:0!model/q_dense_1/clip_by_value:z:0*
T0*
_output_shapes

: `
model/q_dense_1/truediv_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   B
model/q_dense_1/truediv_1RealDivmodel/q_dense_1/mul_1:z:0$model/q_dense_1/truediv_1/y:output:0*
T0*
_output_shapes

: \
model/q_dense_1/mul_2/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?
model/q_dense_1/mul_2Mul model/q_dense_1/mul_2/x:output:0model/q_dense_1/truediv_1:z:0*
T0*
_output_shapes

: 
 model/q_dense_1/ReadVariableOp_1ReadVariableOp'model_q_dense_1_readvariableop_resource*
_output_shapes

: *
dtype0o
model/q_dense_1/Neg_1Neg(model/q_dense_1/ReadVariableOp_1:value:0*
T0*
_output_shapes

: }
model/q_dense_1/add_2AddV2model/q_dense_1/Neg_1:y:0model/q_dense_1/mul_2:z:0*
T0*
_output_shapes

: \
model/q_dense_1/mul_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?
model/q_dense_1/mul_3Mul model/q_dense_1/mul_3/x:output:0model/q_dense_1/add_2:z:0*
T0*
_output_shapes

: r
model/q_dense_1/StopGradient_1StopGradientmodel/q_dense_1/mul_3:z:0*
T0*
_output_shapes

: 
 model/q_dense_1/ReadVariableOp_2ReadVariableOp'model_q_dense_1_readvariableop_resource*
_output_shapes

: *
dtype0
model/q_dense_1/add_3AddV2(model/q_dense_1/ReadVariableOp_2:value:0'model/q_dense_1/StopGradient_1:output:0*
T0*
_output_shapes

: 
model/q_dense_1/MatMulMatMulmodel/q_dense/add_11:z:0model/q_dense_1/add_3:z:0*
T0*'
_output_shapes
:?????????Y
model/q_dense_1/Pow_1/xConst*
_output_shapes
: *
dtype0*
value	B :Y
model/q_dense_1/Pow_1/yConst*
_output_shapes
: *
dtype0*
value	B :
model/q_dense_1/Pow_1Pow model/q_dense_1/Pow_1/x:output:0 model/q_dense_1/Pow_1/y:output:0*
T0*
_output_shapes
: i
model/q_dense_1/Cast_1Castmodel/q_dense_1/Pow_1:z:0*

DstT0*

SrcT0*
_output_shapes
: 
 model/q_dense_1/ReadVariableOp_3ReadVariableOp)model_q_dense_1_readvariableop_3_resource*
_output_shapes
:*
dtype0\
model/q_dense_1/mul_4/yConst*
_output_shapes
: *
dtype0*
valueB
 *  E
model/q_dense_1/mul_4Mul(model/q_dense_1/ReadVariableOp_3:value:0 model/q_dense_1/mul_4/y:output:0*
T0*
_output_shapes
:
model/q_dense_1/truediv_2RealDivmodel/q_dense_1/mul_4:z:0model/q_dense_1/Cast_1:y:0*
T0*
_output_shapes
:`
model/q_dense_1/Neg_2Negmodel/q_dense_1/truediv_2:z:0*
T0*
_output_shapes
:d
model/q_dense_1/Round_1Roundmodel/q_dense_1/truediv_2:z:0*
T0*
_output_shapes
:{
model/q_dense_1/add_4AddV2model/q_dense_1/Neg_2:y:0model/q_dense_1/Round_1:y:0*
T0*
_output_shapes
:n
model/q_dense_1/StopGradient_2StopGradientmodel/q_dense_1/add_4:z:0*
T0*
_output_shapes
:
model/q_dense_1/add_5AddV2model/q_dense_1/truediv_2:z:0'model/q_dense_1/StopGradient_2:output:0*
T0*
_output_shapes
:n
)model/q_dense_1/clip_by_value_1/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * πE¦
'model/q_dense_1/clip_by_value_1/MinimumMinimummodel/q_dense_1/add_5:z:02model/q_dense_1/clip_by_value_1/Minimum/y:output:0*
T0*
_output_shapes
:f
!model/q_dense_1/clip_by_value_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *  Ε¨
model/q_dense_1/clip_by_value_1Maximum+model/q_dense_1/clip_by_value_1/Minimum:z:0*model/q_dense_1/clip_by_value_1/y:output:0*
T0*
_output_shapes
:
model/q_dense_1/mul_5Mulmodel/q_dense_1/Cast_1:y:0#model/q_dense_1/clip_by_value_1:z:0*
T0*
_output_shapes
:`
model/q_dense_1/truediv_3/yConst*
_output_shapes
: *
dtype0*
valueB
 *  E
model/q_dense_1/truediv_3RealDivmodel/q_dense_1/mul_5:z:0$model/q_dense_1/truediv_3/y:output:0*
T0*
_output_shapes
:\
model/q_dense_1/mul_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?
model/q_dense_1/mul_6Mul model/q_dense_1/mul_6/x:output:0model/q_dense_1/truediv_3:z:0*
T0*
_output_shapes
:
 model/q_dense_1/ReadVariableOp_4ReadVariableOp)model_q_dense_1_readvariableop_3_resource*
_output_shapes
:*
dtype0k
model/q_dense_1/Neg_3Neg(model/q_dense_1/ReadVariableOp_4:value:0*
T0*
_output_shapes
:y
model/q_dense_1/add_6AddV2model/q_dense_1/Neg_3:y:0model/q_dense_1/mul_6:z:0*
T0*
_output_shapes
:\
model/q_dense_1/mul_7/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?~
model/q_dense_1/mul_7Mul model/q_dense_1/mul_7/x:output:0model/q_dense_1/add_6:z:0*
T0*
_output_shapes
:n
model/q_dense_1/StopGradient_3StopGradientmodel/q_dense_1/mul_7:z:0*
T0*
_output_shapes
:
 model/q_dense_1/ReadVariableOp_5ReadVariableOp)model_q_dense_1_readvariableop_3_resource*
_output_shapes
:*
dtype0
model/q_dense_1/add_7AddV2(model/q_dense_1/ReadVariableOp_5:value:0'model/q_dense_1/StopGradient_3:output:0*
T0*
_output_shapes
:
model/q_dense_1/BiasAddBiasAdd model/q_dense_1/MatMul:product:0model/q_dense_1/add_7:z:0*
T0*'
_output_shapes
:?????????Y
model/q_dense_1/Pow_2/xConst*
_output_shapes
: *
dtype0*
value	B :Y
model/q_dense_1/Pow_2/yConst*
_output_shapes
: *
dtype0*
value	B :
model/q_dense_1/Pow_2Pow model/q_dense_1/Pow_2/x:output:0 model/q_dense_1/Pow_2/y:output:0*
T0*
_output_shapes
: i
model/q_dense_1/Cast_2Castmodel/q_dense_1/Pow_2:z:0*

DstT0*

SrcT0*
_output_shapes
: Y
model/q_dense_1/Pow_3/xConst*
_output_shapes
: *
dtype0*
value	B :Y
model/q_dense_1/Pow_3/yConst*
_output_shapes
: *
dtype0*
value	B :
model/q_dense_1/Pow_3Pow model/q_dense_1/Pow_3/x:output:0 model/q_dense_1/Pow_3/y:output:0*
T0*
_output_shapes
: i
model/q_dense_1/Cast_3Castmodel/q_dense_1/Pow_3:z:0*

DstT0*

SrcT0*
_output_shapes
: Z
model/q_dense_1/ConstConst*
_output_shapes
: *
dtype0*
valueB
 *   @Z
model/q_dense_1/Cast_4/xConst*
_output_shapes
: *
dtype0*
value	B :q
model/q_dense_1/Cast_4Cast!model/q_dense_1/Cast_4/x:output:0*

DstT0*

SrcT0*
_output_shapes
: Z
model/q_dense_1/sub/yConst*
_output_shapes
: *
dtype0*
valueB
 *  PAw
model/q_dense_1/subSubmodel/q_dense_1/Cast_4:y:0model/q_dense_1/sub/y:output:0*
T0*
_output_shapes
: v
model/q_dense_1/Pow_4Powmodel/q_dense_1/Const:output:0model/q_dense_1/sub:z:0*
T0*
_output_shapes
: t
model/q_dense_1/sub_1Submodel/q_dense_1/Cast_3:y:0model/q_dense_1/Pow_4:z:0*
T0*
_output_shapes
: 
model/q_dense_1/LessEqual	LessEqual model/q_dense_1/BiasAdd:output:0model/q_dense_1/sub_1:z:0*
T0*'
_output_shapes
:?????????p
model/q_dense_1/ReluRelu model/q_dense_1/BiasAdd:output:0*
T0*'
_output_shapes
:?????????o
model/q_dense_1/ones_like/ShapeShape model/q_dense_1/BiasAdd:output:0*
T0*
_output_shapes
:d
model/q_dense_1/ones_like/ConstConst*
_output_shapes
: *
dtype0*
valueB
 *  ?§
model/q_dense_1/ones_likeFill(model/q_dense_1/ones_like/Shape:output:0(model/q_dense_1/ones_like/Const:output:0*
T0*'
_output_shapes
:?????????t
model/q_dense_1/sub_2Submodel/q_dense_1/Cast_3:y:0model/q_dense_1/Pow_4:z:0*
T0*
_output_shapes
: 
model/q_dense_1/mul_8Mul"model/q_dense_1/ones_like:output:0model/q_dense_1/sub_2:z:0*
T0*'
_output_shapes
:?????????΄
model/q_dense_1/SelectV2SelectV2model/q_dense_1/LessEqual:z:0"model/q_dense_1/Relu:activations:0model/q_dense_1/mul_8:z:0*
T0*'
_output_shapes
:?????????
model/q_dense_1/mul_9Mul model/q_dense_1/BiasAdd:output:0model/q_dense_1/Cast_2:y:0*
T0*'
_output_shapes
:?????????
model/q_dense_1/truediv_4RealDivmodel/q_dense_1/mul_9:z:0model/q_dense_1/Cast_3:y:0*
T0*'
_output_shapes
:?????????m
model/q_dense_1/Neg_4Negmodel/q_dense_1/truediv_4:z:0*
T0*'
_output_shapes
:?????????q
model/q_dense_1/Round_2Roundmodel/q_dense_1/truediv_4:z:0*
T0*'
_output_shapes
:?????????
model/q_dense_1/add_8AddV2model/q_dense_1/Neg_4:y:0model/q_dense_1/Round_2:y:0*
T0*'
_output_shapes
:?????????{
model/q_dense_1/StopGradient_4StopGradientmodel/q_dense_1/add_8:z:0*
T0*'
_output_shapes
:?????????
model/q_dense_1/add_9AddV2model/q_dense_1/truediv_4:z:0'model/q_dense_1/StopGradient_4:output:0*
T0*'
_output_shapes
:?????????
model/q_dense_1/truediv_5RealDivmodel/q_dense_1/add_9:z:0model/q_dense_1/Cast_2:y:0*
T0*'
_output_shapes
:?????????`
model/q_dense_1/truediv_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?
model/q_dense_1/truediv_6RealDiv$model/q_dense_1/truediv_6/x:output:0model/q_dense_1/Cast_2:y:0*
T0*
_output_shapes
: \
model/q_dense_1/sub_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?~
model/q_dense_1/sub_3Sub model/q_dense_1/sub_3/x:output:0model/q_dense_1/truediv_6:z:0*
T0*
_output_shapes
: 
'model/q_dense_1/clip_by_value_2/MinimumMinimummodel/q_dense_1/truediv_5:z:0model/q_dense_1/sub_3:z:0*
T0*'
_output_shapes
:?????????f
!model/q_dense_1/clip_by_value_2/yConst*
_output_shapes
: *
dtype0*
valueB
 *    ΅
model/q_dense_1/clip_by_value_2Maximum+model/q_dense_1/clip_by_value_2/Minimum:z:0*model/q_dense_1/clip_by_value_2/y:output:0*
T0*'
_output_shapes
:?????????
model/q_dense_1/mul_10Mulmodel/q_dense_1/Cast_3:y:0#model/q_dense_1/clip_by_value_2:z:0*
T0*'
_output_shapes
:?????????q
model/q_dense_1/Neg_5Neg!model/q_dense_1/SelectV2:output:0*
T0*'
_output_shapes
:?????????
model/q_dense_1/add_10AddV2model/q_dense_1/Neg_5:y:0model/q_dense_1/mul_10:z:0*
T0*'
_output_shapes
:?????????]
model/q_dense_1/mul_11/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?
model/q_dense_1/mul_11Mul!model/q_dense_1/mul_11/x:output:0model/q_dense_1/add_10:z:0*
T0*'
_output_shapes
:?????????|
model/q_dense_1/StopGradient_5StopGradientmodel/q_dense_1/mul_11:z:0*
T0*'
_output_shapes
:?????????
model/q_dense_1/add_11AddV2!model/q_dense_1/SelectV2:output:0'model/q_dense_1/StopGradient_5:output:0*
T0*'
_output_shapes
:?????????P
model/mu/Pow/xConst*
_output_shapes
: *
dtype0*
value	B :P
model/mu/Pow/yConst*
_output_shapes
: *
dtype0*
value	B :f
model/mu/PowPowmodel/mu/Pow/x:output:0model/mu/Pow/y:output:0*
T0*
_output_shapes
: W
model/mu/CastCastmodel/mu/Pow:z:0*

DstT0*

SrcT0*
_output_shapes
: x
model/mu/ReadVariableOpReadVariableOp model_mu_readvariableop_resource*
_output_shapes

:*
dtype0S
model/mu/mul/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Bv
model/mu/mulMulmodel/mu/ReadVariableOp:value:0model/mu/mul/y:output:0*
T0*
_output_shapes

:i
model/mu/truedivRealDivmodel/mu/mul:z:0model/mu/Cast:y:0*
T0*
_output_shapes

:R
model/mu/NegNegmodel/mu/truediv:z:0*
T0*
_output_shapes

:V
model/mu/RoundRoundmodel/mu/truediv:z:0*
T0*
_output_shapes

:d
model/mu/addAddV2model/mu/Neg:y:0model/mu/Round:y:0*
T0*
_output_shapes

:`
model/mu/StopGradientStopGradientmodel/mu/add:z:0*
T0*
_output_shapes

:v
model/mu/add_1AddV2model/mu/truediv:z:0model/mu/StopGradient:output:0*
T0*
_output_shapes

:e
 model/mu/clip_by_value/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 *  ψA
model/mu/clip_by_value/MinimumMinimummodel/mu/add_1:z:0)model/mu/clip_by_value/Minimum/y:output:0*
T0*
_output_shapes

:]
model/mu/clip_by_value/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Β
model/mu/clip_by_valueMaximum"model/mu/clip_by_value/Minimum:z:0!model/mu/clip_by_value/y:output:0*
T0*
_output_shapes

:m
model/mu/mul_1Mulmodel/mu/Cast:y:0model/mu/clip_by_value:z:0*
T0*
_output_shapes

:Y
model/mu/truediv_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   By
model/mu/truediv_1RealDivmodel/mu/mul_1:z:0model/mu/truediv_1/y:output:0*
T0*
_output_shapes

:U
model/mu/mul_2/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?q
model/mu/mul_2Mulmodel/mu/mul_2/x:output:0model/mu/truediv_1:z:0*
T0*
_output_shapes

:z
model/mu/ReadVariableOp_1ReadVariableOp model_mu_readvariableop_resource*
_output_shapes

:*
dtype0a
model/mu/Neg_1Neg!model/mu/ReadVariableOp_1:value:0*
T0*
_output_shapes

:h
model/mu/add_2AddV2model/mu/Neg_1:y:0model/mu/mul_2:z:0*
T0*
_output_shapes

:U
model/mu/mul_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?m
model/mu/mul_3Mulmodel/mu/mul_3/x:output:0model/mu/add_2:z:0*
T0*
_output_shapes

:d
model/mu/StopGradient_1StopGradientmodel/mu/mul_3:z:0*
T0*
_output_shapes

:z
model/mu/ReadVariableOp_2ReadVariableOp model_mu_readvariableop_resource*
_output_shapes

:*
dtype0
model/mu/add_3AddV2!model/mu/ReadVariableOp_2:value:0 model/mu/StopGradient_1:output:0*
T0*
_output_shapes

:{
model/mu/MatMulMatMulmodel/q_dense_1/add_11:z:0model/mu/add_3:z:0*
T0*'
_output_shapes
:?????????R
model/mu/Pow_1/xConst*
_output_shapes
: *
dtype0*
value	B :R
model/mu/Pow_1/yConst*
_output_shapes
: *
dtype0*
value	B :l
model/mu/Pow_1Powmodel/mu/Pow_1/x:output:0model/mu/Pow_1/y:output:0*
T0*
_output_shapes
: [
model/mu/Cast_1Castmodel/mu/Pow_1:z:0*

DstT0*

SrcT0*
_output_shapes
: x
model/mu/ReadVariableOp_3ReadVariableOp"model_mu_readvariableop_3_resource*
_output_shapes
:*
dtype0U
model/mu/mul_4/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Dx
model/mu/mul_4Mul!model/mu/ReadVariableOp_3:value:0model/mu/mul_4/y:output:0*
T0*
_output_shapes
:k
model/mu/truediv_2RealDivmodel/mu/mul_4:z:0model/mu/Cast_1:y:0*
T0*
_output_shapes
:R
model/mu/Neg_2Negmodel/mu/truediv_2:z:0*
T0*
_output_shapes
:V
model/mu/Round_1Roundmodel/mu/truediv_2:z:0*
T0*
_output_shapes
:f
model/mu/add_4AddV2model/mu/Neg_2:y:0model/mu/Round_1:y:0*
T0*
_output_shapes
:`
model/mu/StopGradient_2StopGradientmodel/mu/add_4:z:0*
T0*
_output_shapes
:v
model/mu/add_5AddV2model/mu/truediv_2:z:0 model/mu/StopGradient_2:output:0*
T0*
_output_shapes
:g
"model/mu/clip_by_value_1/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * ?C
 model/mu/clip_by_value_1/MinimumMinimummodel/mu/add_5:z:0+model/mu/clip_by_value_1/Minimum/y:output:0*
T0*
_output_shapes
:_
model/mu/clip_by_value_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Δ
model/mu/clip_by_value_1Maximum$model/mu/clip_by_value_1/Minimum:z:0#model/mu/clip_by_value_1/y:output:0*
T0*
_output_shapes
:m
model/mu/mul_5Mulmodel/mu/Cast_1:y:0model/mu/clip_by_value_1:z:0*
T0*
_output_shapes
:Y
model/mu/truediv_3/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Du
model/mu/truediv_3RealDivmodel/mu/mul_5:z:0model/mu/truediv_3/y:output:0*
T0*
_output_shapes
:U
model/mu/mul_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?m
model/mu/mul_6Mulmodel/mu/mul_6/x:output:0model/mu/truediv_3:z:0*
T0*
_output_shapes
:x
model/mu/ReadVariableOp_4ReadVariableOp"model_mu_readvariableop_3_resource*
_output_shapes
:*
dtype0]
model/mu/Neg_3Neg!model/mu/ReadVariableOp_4:value:0*
T0*
_output_shapes
:d
model/mu/add_6AddV2model/mu/Neg_3:y:0model/mu/mul_6:z:0*
T0*
_output_shapes
:U
model/mu/mul_7/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?i
model/mu/mul_7Mulmodel/mu/mul_7/x:output:0model/mu/add_6:z:0*
T0*
_output_shapes
:`
model/mu/StopGradient_3StopGradientmodel/mu/mul_7:z:0*
T0*
_output_shapes
:x
model/mu/ReadVariableOp_5ReadVariableOp"model_mu_readvariableop_3_resource*
_output_shapes
:*
dtype0
model/mu/add_7AddV2!model/mu/ReadVariableOp_5:value:0 model/mu/StopGradient_3:output:0*
T0*
_output_shapes
:|
model/mu/BiasAddBiasAddmodel/mu/MatMul:product:0model/mu/add_7:z:0*
T0*'
_output_shapes
:?????????R
model/mu/Pow_2/xConst*
_output_shapes
: *
dtype0*
value	B :R
model/mu/Pow_2/yConst*
_output_shapes
: *
dtype0*
value	B :l
model/mu/Pow_2Powmodel/mu/Pow_2/x:output:0model/mu/Pow_2/y:output:0*
T0*
_output_shapes
: [
model/mu/Cast_2Castmodel/mu/Pow_2:z:0*

DstT0*

SrcT0*
_output_shapes
: U
model/mu/mul_8/yConst*
_output_shapes
: *
dtype0*
valueB
 *   D}
model/mu/mul_8Mulmodel/mu/BiasAdd:output:0model/mu/mul_8/y:output:0*
T0*'
_output_shapes
:?????????x
model/mu/truediv_4RealDivmodel/mu/mul_8:z:0model/mu/Cast_2:y:0*
T0*'
_output_shapes
:?????????_
model/mu/Neg_4Negmodel/mu/truediv_4:z:0*
T0*'
_output_shapes
:?????????c
model/mu/Round_2Roundmodel/mu/truediv_4:z:0*
T0*'
_output_shapes
:?????????s
model/mu/add_8AddV2model/mu/Neg_4:y:0model/mu/Round_2:y:0*
T0*'
_output_shapes
:?????????m
model/mu/StopGradient_4StopGradientmodel/mu/add_8:z:0*
T0*'
_output_shapes
:?????????
model/mu/add_9AddV2model/mu/truediv_4:z:0 model/mu/StopGradient_4:output:0*
T0*'
_output_shapes
:?????????g
"model/mu/clip_by_value_2/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * ?C
 model/mu/clip_by_value_2/MinimumMinimummodel/mu/add_9:z:0+model/mu/clip_by_value_2/Minimum/y:output:0*
T0*'
_output_shapes
:?????????_
model/mu/clip_by_value_2/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Δ 
model/mu/clip_by_value_2Maximum$model/mu/clip_by_value_2/Minimum:z:0#model/mu/clip_by_value_2/y:output:0*
T0*'
_output_shapes
:?????????z
model/mu/mul_9Mulmodel/mu/Cast_2:y:0model/mu/clip_by_value_2:z:0*
T0*'
_output_shapes
:?????????Y
model/mu/truediv_5/yConst*
_output_shapes
: *
dtype0*
valueB
 *   D
model/mu/truediv_5RealDivmodel/mu/mul_9:z:0model/mu/truediv_5/y:output:0*
T0*'
_output_shapes
:?????????V
model/mu/mul_10/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?|
model/mu/mul_10Mulmodel/mu/mul_10/x:output:0model/mu/truediv_5:z:0*
T0*'
_output_shapes
:?????????b
model/mu/Neg_5Negmodel/mu/BiasAdd:output:0*
T0*'
_output_shapes
:?????????s
model/mu/add_10AddV2model/mu/Neg_5:y:0model/mu/mul_10:z:0*
T0*'
_output_shapes
:?????????V
model/mu/mul_11/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?y
model/mu/mul_11Mulmodel/mu/mul_11/x:output:0model/mu/add_10:z:0*
T0*'
_output_shapes
:?????????n
model/mu/StopGradient_5StopGradientmodel/mu/mul_11:z:0*
T0*'
_output_shapes
:?????????
model/mu/add_11AddV2model/mu/BiasAdd:output:0 model/mu/StopGradient_5:output:0*
T0*'
_output_shapes
:?????????b
IdentityIdentitymodel/mu/add_11:z:0^NoOp*
T0*'
_output_shapes
:?????????
NoOpNoOp^model/mu/ReadVariableOp^model/mu/ReadVariableOp_1^model/mu/ReadVariableOp_2^model/mu/ReadVariableOp_3^model/mu/ReadVariableOp_4^model/mu/ReadVariableOp_5^model/q_dense/ReadVariableOp^model/q_dense/ReadVariableOp_1^model/q_dense/ReadVariableOp_2^model/q_dense/ReadVariableOp_3^model/q_dense/ReadVariableOp_4^model/q_dense/ReadVariableOp_5^model/q_dense_1/ReadVariableOp!^model/q_dense_1/ReadVariableOp_1!^model/q_dense_1/ReadVariableOp_2!^model/q_dense_1/ReadVariableOp_3!^model/q_dense_1/ReadVariableOp_4!^model/q_dense_1/ReadVariableOp_5*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*2
_input_shapes!
:?????????9: : : : : : 22
model/mu/ReadVariableOpmodel/mu/ReadVariableOp26
model/mu/ReadVariableOp_1model/mu/ReadVariableOp_126
model/mu/ReadVariableOp_2model/mu/ReadVariableOp_226
model/mu/ReadVariableOp_3model/mu/ReadVariableOp_326
model/mu/ReadVariableOp_4model/mu/ReadVariableOp_426
model/mu/ReadVariableOp_5model/mu/ReadVariableOp_52<
model/q_dense/ReadVariableOpmodel/q_dense/ReadVariableOp2@
model/q_dense/ReadVariableOp_1model/q_dense/ReadVariableOp_12@
model/q_dense/ReadVariableOp_2model/q_dense/ReadVariableOp_22@
model/q_dense/ReadVariableOp_3model/q_dense/ReadVariableOp_32@
model/q_dense/ReadVariableOp_4model/q_dense/ReadVariableOp_42@
model/q_dense/ReadVariableOp_5model/q_dense/ReadVariableOp_52@
model/q_dense_1/ReadVariableOpmodel/q_dense_1/ReadVariableOp2D
 model/q_dense_1/ReadVariableOp_1 model/q_dense_1/ReadVariableOp_12D
 model/q_dense_1/ReadVariableOp_2 model/q_dense_1/ReadVariableOp_22D
 model/q_dense_1/ReadVariableOp_3 model/q_dense_1/ReadVariableOp_32D
 model/q_dense_1/ReadVariableOp_4 model/q_dense_1/ReadVariableOp_42D
 model/q_dense_1/ReadVariableOp_5 model/q_dense_1/ReadVariableOp_5:P L
'
_output_shapes
:?????????9
!
_user_specified_name	input_1
Υ²
΄
?__inference_model_layer_call_and_return_conditional_losses_2158

inputs1
q_dense_readvariableop_resource:9 /
!q_dense_readvariableop_3_resource: 3
!q_dense_1_readvariableop_resource: 1
#q_dense_1_readvariableop_3_resource:,
mu_readvariableop_resource:*
mu_readvariableop_3_resource:
identity’mu/ReadVariableOp’mu/ReadVariableOp_1’mu/ReadVariableOp_2’mu/ReadVariableOp_3’mu/ReadVariableOp_4’mu/ReadVariableOp_5’q_dense/ReadVariableOp’q_dense/ReadVariableOp_1’q_dense/ReadVariableOp_2’q_dense/ReadVariableOp_3’q_dense/ReadVariableOp_4’q_dense/ReadVariableOp_5’-q_dense/kernel/Regularizer/Abs/ReadVariableOp’q_dense_1/ReadVariableOp’q_dense_1/ReadVariableOp_1’q_dense_1/ReadVariableOp_2’q_dense_1/ReadVariableOp_3’q_dense_1/ReadVariableOp_4’q_dense_1/ReadVariableOp_5’/q_dense_1/kernel/Regularizer/Abs/ReadVariableOpT
q_activation/Pow/xConst*
_output_shapes
: *
dtype0*
value	B :T
q_activation/Pow/yConst*
_output_shapes
: *
dtype0*
value	B :r
q_activation/PowPowq_activation/Pow/x:output:0q_activation/Pow/y:output:0*
T0*
_output_shapes
: _
q_activation/CastCastq_activation/Pow:z:0*

DstT0*

SrcT0*
_output_shapes
: W
q_activation/mul/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Dn
q_activation/mulMulinputsq_activation/mul/y:output:0*
T0*'
_output_shapes
:?????????9~
q_activation/truedivRealDivq_activation/mul:z:0q_activation/Cast:y:0*
T0*'
_output_shapes
:?????????9c
q_activation/NegNegq_activation/truediv:z:0*
T0*'
_output_shapes
:?????????9g
q_activation/RoundRoundq_activation/truediv:z:0*
T0*'
_output_shapes
:?????????9y
q_activation/addAddV2q_activation/Neg:y:0q_activation/Round:y:0*
T0*'
_output_shapes
:?????????9q
q_activation/StopGradientStopGradientq_activation/add:z:0*
T0*'
_output_shapes
:?????????9
q_activation/add_1AddV2q_activation/truediv:z:0"q_activation/StopGradient:output:0*
T0*'
_output_shapes
:?????????9i
$q_activation/clip_by_value/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * ?C¦
"q_activation/clip_by_value/MinimumMinimumq_activation/add_1:z:0-q_activation/clip_by_value/Minimum/y:output:0*
T0*'
_output_shapes
:?????????9a
q_activation/clip_by_value/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Δ¦
q_activation/clip_by_valueMaximum&q_activation/clip_by_value/Minimum:z:0%q_activation/clip_by_value/y:output:0*
T0*'
_output_shapes
:?????????9
q_activation/mul_1Mulq_activation/Cast:y:0q_activation/clip_by_value:z:0*
T0*'
_output_shapes
:?????????9]
q_activation/truediv_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   D
q_activation/truediv_1RealDivq_activation/mul_1:z:0!q_activation/truediv_1/y:output:0*
T0*'
_output_shapes
:?????????9Y
q_activation/mul_2/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?
q_activation/mul_2Mulq_activation/mul_2/x:output:0q_activation/truediv_1:z:0*
T0*'
_output_shapes
:?????????9S
q_activation/Neg_1Neginputs*
T0*'
_output_shapes
:?????????9}
q_activation/add_2AddV2q_activation/Neg_1:y:0q_activation/mul_2:z:0*
T0*'
_output_shapes
:?????????9Y
q_activation/mul_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?
q_activation/mul_3Mulq_activation/mul_3/x:output:0q_activation/add_2:z:0*
T0*'
_output_shapes
:?????????9u
q_activation/StopGradient_1StopGradientq_activation/mul_3:z:0*
T0*'
_output_shapes
:?????????9{
q_activation/add_3AddV2inputs$q_activation/StopGradient_1:output:0*
T0*'
_output_shapes
:?????????9O
q_dense/Pow/xConst*
_output_shapes
: *
dtype0*
value	B :O
q_dense/Pow/yConst*
_output_shapes
: *
dtype0*
value	B :c
q_dense/PowPowq_dense/Pow/x:output:0q_dense/Pow/y:output:0*
T0*
_output_shapes
: U
q_dense/CastCastq_dense/Pow:z:0*

DstT0*

SrcT0*
_output_shapes
: v
q_dense/ReadVariableOpReadVariableOpq_dense_readvariableop_resource*
_output_shapes

:9 *
dtype0R
q_dense/mul/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Bs
q_dense/mulMulq_dense/ReadVariableOp:value:0q_dense/mul/y:output:0*
T0*
_output_shapes

:9 f
q_dense/truedivRealDivq_dense/mul:z:0q_dense/Cast:y:0*
T0*
_output_shapes

:9 P
q_dense/NegNegq_dense/truediv:z:0*
T0*
_output_shapes

:9 T
q_dense/RoundRoundq_dense/truediv:z:0*
T0*
_output_shapes

:9 a
q_dense/addAddV2q_dense/Neg:y:0q_dense/Round:y:0*
T0*
_output_shapes

:9 ^
q_dense/StopGradientStopGradientq_dense/add:z:0*
T0*
_output_shapes

:9 s
q_dense/add_1AddV2q_dense/truediv:z:0q_dense/StopGradient:output:0*
T0*
_output_shapes

:9 d
q_dense/clip_by_value/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 *  ψA
q_dense/clip_by_value/MinimumMinimumq_dense/add_1:z:0(q_dense/clip_by_value/Minimum/y:output:0*
T0*
_output_shapes

:9 \
q_dense/clip_by_value/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Β
q_dense/clip_by_valueMaximum!q_dense/clip_by_value/Minimum:z:0 q_dense/clip_by_value/y:output:0*
T0*
_output_shapes

:9 j
q_dense/mul_1Mulq_dense/Cast:y:0q_dense/clip_by_value:z:0*
T0*
_output_shapes

:9 X
q_dense/truediv_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Bv
q_dense/truediv_1RealDivq_dense/mul_1:z:0q_dense/truediv_1/y:output:0*
T0*
_output_shapes

:9 T
q_dense/mul_2/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?n
q_dense/mul_2Mulq_dense/mul_2/x:output:0q_dense/truediv_1:z:0*
T0*
_output_shapes

:9 x
q_dense/ReadVariableOp_1ReadVariableOpq_dense_readvariableop_resource*
_output_shapes

:9 *
dtype0_
q_dense/Neg_1Neg q_dense/ReadVariableOp_1:value:0*
T0*
_output_shapes

:9 e
q_dense/add_2AddV2q_dense/Neg_1:y:0q_dense/mul_2:z:0*
T0*
_output_shapes

:9 T
q_dense/mul_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?j
q_dense/mul_3Mulq_dense/mul_3/x:output:0q_dense/add_2:z:0*
T0*
_output_shapes

:9 b
q_dense/StopGradient_1StopGradientq_dense/mul_3:z:0*
T0*
_output_shapes

:9 x
q_dense/ReadVariableOp_2ReadVariableOpq_dense_readvariableop_resource*
_output_shapes

:9 *
dtype0
q_dense/add_3AddV2 q_dense/ReadVariableOp_2:value:0q_dense/StopGradient_1:output:0*
T0*
_output_shapes

:9 u
q_dense/MatMulMatMulq_activation/add_3:z:0q_dense/add_3:z:0*
T0*'
_output_shapes
:????????? Q
q_dense/Pow_1/xConst*
_output_shapes
: *
dtype0*
value	B :Q
q_dense/Pow_1/yConst*
_output_shapes
: *
dtype0*
value	B :i
q_dense/Pow_1Powq_dense/Pow_1/x:output:0q_dense/Pow_1/y:output:0*
T0*
_output_shapes
: Y
q_dense/Cast_1Castq_dense/Pow_1:z:0*

DstT0*

SrcT0*
_output_shapes
: v
q_dense/ReadVariableOp_3ReadVariableOp!q_dense_readvariableop_3_resource*
_output_shapes
: *
dtype0T
q_dense/mul_4/yConst*
_output_shapes
: *
dtype0*
valueB
 *  Eu
q_dense/mul_4Mul q_dense/ReadVariableOp_3:value:0q_dense/mul_4/y:output:0*
T0*
_output_shapes
: h
q_dense/truediv_2RealDivq_dense/mul_4:z:0q_dense/Cast_1:y:0*
T0*
_output_shapes
: P
q_dense/Neg_2Negq_dense/truediv_2:z:0*
T0*
_output_shapes
: T
q_dense/Round_1Roundq_dense/truediv_2:z:0*
T0*
_output_shapes
: c
q_dense/add_4AddV2q_dense/Neg_2:y:0q_dense/Round_1:y:0*
T0*
_output_shapes
: ^
q_dense/StopGradient_2StopGradientq_dense/add_4:z:0*
T0*
_output_shapes
: s
q_dense/add_5AddV2q_dense/truediv_2:z:0q_dense/StopGradient_2:output:0*
T0*
_output_shapes
: f
!q_dense/clip_by_value_1/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * πE
q_dense/clip_by_value_1/MinimumMinimumq_dense/add_5:z:0*q_dense/clip_by_value_1/Minimum/y:output:0*
T0*
_output_shapes
: ^
q_dense/clip_by_value_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *  Ε
q_dense/clip_by_value_1Maximum#q_dense/clip_by_value_1/Minimum:z:0"q_dense/clip_by_value_1/y:output:0*
T0*
_output_shapes
: j
q_dense/mul_5Mulq_dense/Cast_1:y:0q_dense/clip_by_value_1:z:0*
T0*
_output_shapes
: X
q_dense/truediv_3/yConst*
_output_shapes
: *
dtype0*
valueB
 *  Er
q_dense/truediv_3RealDivq_dense/mul_5:z:0q_dense/truediv_3/y:output:0*
T0*
_output_shapes
: T
q_dense/mul_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?j
q_dense/mul_6Mulq_dense/mul_6/x:output:0q_dense/truediv_3:z:0*
T0*
_output_shapes
: v
q_dense/ReadVariableOp_4ReadVariableOp!q_dense_readvariableop_3_resource*
_output_shapes
: *
dtype0[
q_dense/Neg_3Neg q_dense/ReadVariableOp_4:value:0*
T0*
_output_shapes
: a
q_dense/add_6AddV2q_dense/Neg_3:y:0q_dense/mul_6:z:0*
T0*
_output_shapes
: T
q_dense/mul_7/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?f
q_dense/mul_7Mulq_dense/mul_7/x:output:0q_dense/add_6:z:0*
T0*
_output_shapes
: ^
q_dense/StopGradient_3StopGradientq_dense/mul_7:z:0*
T0*
_output_shapes
: v
q_dense/ReadVariableOp_5ReadVariableOp!q_dense_readvariableop_3_resource*
_output_shapes
: *
dtype0~
q_dense/add_7AddV2 q_dense/ReadVariableOp_5:value:0q_dense/StopGradient_3:output:0*
T0*
_output_shapes
: y
q_dense/BiasAddBiasAddq_dense/MatMul:product:0q_dense/add_7:z:0*
T0*'
_output_shapes
:????????? Q
q_dense/Pow_2/xConst*
_output_shapes
: *
dtype0*
value	B :Q
q_dense/Pow_2/yConst*
_output_shapes
: *
dtype0*
value	B :i
q_dense/Pow_2Powq_dense/Pow_2/x:output:0q_dense/Pow_2/y:output:0*
T0*
_output_shapes
: Y
q_dense/Cast_2Castq_dense/Pow_2:z:0*

DstT0*

SrcT0*
_output_shapes
: Q
q_dense/Pow_3/xConst*
_output_shapes
: *
dtype0*
value	B :Q
q_dense/Pow_3/yConst*
_output_shapes
: *
dtype0*
value	B :i
q_dense/Pow_3Powq_dense/Pow_3/x:output:0q_dense/Pow_3/y:output:0*
T0*
_output_shapes
: Y
q_dense/Cast_3Castq_dense/Pow_3:z:0*

DstT0*

SrcT0*
_output_shapes
: R
q_dense/ConstConst*
_output_shapes
: *
dtype0*
valueB
 *   @R
q_dense/Cast_4/xConst*
_output_shapes
: *
dtype0*
value	B :a
q_dense/Cast_4Castq_dense/Cast_4/x:output:0*

DstT0*

SrcT0*
_output_shapes
: R
q_dense/sub/yConst*
_output_shapes
: *
dtype0*
valueB
 *  PA_
q_dense/subSubq_dense/Cast_4:y:0q_dense/sub/y:output:0*
T0*
_output_shapes
: ^
q_dense/Pow_4Powq_dense/Const:output:0q_dense/sub:z:0*
T0*
_output_shapes
: \
q_dense/sub_1Subq_dense/Cast_3:y:0q_dense/Pow_4:z:0*
T0*
_output_shapes
: }
q_dense/LessEqual	LessEqualq_dense/BiasAdd:output:0q_dense/sub_1:z:0*
T0*'
_output_shapes
:????????? `
q_dense/ReluReluq_dense/BiasAdd:output:0*
T0*'
_output_shapes
:????????? _
q_dense/ones_like/ShapeShapeq_dense/BiasAdd:output:0*
T0*
_output_shapes
:\
q_dense/ones_like/ConstConst*
_output_shapes
: *
dtype0*
valueB
 *  ?
q_dense/ones_likeFill q_dense/ones_like/Shape:output:0 q_dense/ones_like/Const:output:0*
T0*'
_output_shapes
:????????? \
q_dense/sub_2Subq_dense/Cast_3:y:0q_dense/Pow_4:z:0*
T0*
_output_shapes
: u
q_dense/mul_8Mulq_dense/ones_like:output:0q_dense/sub_2:z:0*
T0*'
_output_shapes
:????????? 
q_dense/SelectV2SelectV2q_dense/LessEqual:z:0q_dense/Relu:activations:0q_dense/mul_8:z:0*
T0*'
_output_shapes
:????????? t
q_dense/mul_9Mulq_dense/BiasAdd:output:0q_dense/Cast_2:y:0*
T0*'
_output_shapes
:????????? u
q_dense/truediv_4RealDivq_dense/mul_9:z:0q_dense/Cast_3:y:0*
T0*'
_output_shapes
:????????? ]
q_dense/Neg_4Negq_dense/truediv_4:z:0*
T0*'
_output_shapes
:????????? a
q_dense/Round_2Roundq_dense/truediv_4:z:0*
T0*'
_output_shapes
:????????? p
q_dense/add_8AddV2q_dense/Neg_4:y:0q_dense/Round_2:y:0*
T0*'
_output_shapes
:????????? k
q_dense/StopGradient_4StopGradientq_dense/add_8:z:0*
T0*'
_output_shapes
:????????? 
q_dense/add_9AddV2q_dense/truediv_4:z:0q_dense/StopGradient_4:output:0*
T0*'
_output_shapes
:????????? u
q_dense/truediv_5RealDivq_dense/add_9:z:0q_dense/Cast_2:y:0*
T0*'
_output_shapes
:????????? X
q_dense/truediv_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?o
q_dense/truediv_6RealDivq_dense/truediv_6/x:output:0q_dense/Cast_2:y:0*
T0*
_output_shapes
: T
q_dense/sub_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?f
q_dense/sub_3Subq_dense/sub_3/x:output:0q_dense/truediv_6:z:0*
T0*
_output_shapes
: 
q_dense/clip_by_value_2/MinimumMinimumq_dense/truediv_5:z:0q_dense/sub_3:z:0*
T0*'
_output_shapes
:????????? ^
q_dense/clip_by_value_2/yConst*
_output_shapes
: *
dtype0*
valueB
 *    
q_dense/clip_by_value_2Maximum#q_dense/clip_by_value_2/Minimum:z:0"q_dense/clip_by_value_2/y:output:0*
T0*'
_output_shapes
:????????? x
q_dense/mul_10Mulq_dense/Cast_3:y:0q_dense/clip_by_value_2:z:0*
T0*'
_output_shapes
:????????? a
q_dense/Neg_5Negq_dense/SelectV2:output:0*
T0*'
_output_shapes
:????????? p
q_dense/add_10AddV2q_dense/Neg_5:y:0q_dense/mul_10:z:0*
T0*'
_output_shapes
:????????? U
q_dense/mul_11/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?v
q_dense/mul_11Mulq_dense/mul_11/x:output:0q_dense/add_10:z:0*
T0*'
_output_shapes
:????????? l
q_dense/StopGradient_5StopGradientq_dense/mul_11:z:0*
T0*'
_output_shapes
:????????? 
q_dense/add_11AddV2q_dense/SelectV2:output:0q_dense/StopGradient_5:output:0*
T0*'
_output_shapes
:????????? Q
q_dense_1/Pow/xConst*
_output_shapes
: *
dtype0*
value	B :Q
q_dense_1/Pow/yConst*
_output_shapes
: *
dtype0*
value	B :i
q_dense_1/PowPowq_dense_1/Pow/x:output:0q_dense_1/Pow/y:output:0*
T0*
_output_shapes
: Y
q_dense_1/CastCastq_dense_1/Pow:z:0*

DstT0*

SrcT0*
_output_shapes
: z
q_dense_1/ReadVariableOpReadVariableOp!q_dense_1_readvariableop_resource*
_output_shapes

: *
dtype0T
q_dense_1/mul/yConst*
_output_shapes
: *
dtype0*
valueB
 *   By
q_dense_1/mulMul q_dense_1/ReadVariableOp:value:0q_dense_1/mul/y:output:0*
T0*
_output_shapes

: l
q_dense_1/truedivRealDivq_dense_1/mul:z:0q_dense_1/Cast:y:0*
T0*
_output_shapes

: T
q_dense_1/NegNegq_dense_1/truediv:z:0*
T0*
_output_shapes

: X
q_dense_1/RoundRoundq_dense_1/truediv:z:0*
T0*
_output_shapes

: g
q_dense_1/addAddV2q_dense_1/Neg:y:0q_dense_1/Round:y:0*
T0*
_output_shapes

: b
q_dense_1/StopGradientStopGradientq_dense_1/add:z:0*
T0*
_output_shapes

: y
q_dense_1/add_1AddV2q_dense_1/truediv:z:0q_dense_1/StopGradient:output:0*
T0*
_output_shapes

: f
!q_dense_1/clip_by_value/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 *  ψA
q_dense_1/clip_by_value/MinimumMinimumq_dense_1/add_1:z:0*q_dense_1/clip_by_value/Minimum/y:output:0*
T0*
_output_shapes

: ^
q_dense_1/clip_by_value/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Β
q_dense_1/clip_by_valueMaximum#q_dense_1/clip_by_value/Minimum:z:0"q_dense_1/clip_by_value/y:output:0*
T0*
_output_shapes

: p
q_dense_1/mul_1Mulq_dense_1/Cast:y:0q_dense_1/clip_by_value:z:0*
T0*
_output_shapes

: Z
q_dense_1/truediv_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   B|
q_dense_1/truediv_1RealDivq_dense_1/mul_1:z:0q_dense_1/truediv_1/y:output:0*
T0*
_output_shapes

: V
q_dense_1/mul_2/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?t
q_dense_1/mul_2Mulq_dense_1/mul_2/x:output:0q_dense_1/truediv_1:z:0*
T0*
_output_shapes

: |
q_dense_1/ReadVariableOp_1ReadVariableOp!q_dense_1_readvariableop_resource*
_output_shapes

: *
dtype0c
q_dense_1/Neg_1Neg"q_dense_1/ReadVariableOp_1:value:0*
T0*
_output_shapes

: k
q_dense_1/add_2AddV2q_dense_1/Neg_1:y:0q_dense_1/mul_2:z:0*
T0*
_output_shapes

: V
q_dense_1/mul_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?p
q_dense_1/mul_3Mulq_dense_1/mul_3/x:output:0q_dense_1/add_2:z:0*
T0*
_output_shapes

: f
q_dense_1/StopGradient_1StopGradientq_dense_1/mul_3:z:0*
T0*
_output_shapes

: |
q_dense_1/ReadVariableOp_2ReadVariableOp!q_dense_1_readvariableop_resource*
_output_shapes

: *
dtype0
q_dense_1/add_3AddV2"q_dense_1/ReadVariableOp_2:value:0!q_dense_1/StopGradient_1:output:0*
T0*
_output_shapes

: u
q_dense_1/MatMulMatMulq_dense/add_11:z:0q_dense_1/add_3:z:0*
T0*'
_output_shapes
:?????????S
q_dense_1/Pow_1/xConst*
_output_shapes
: *
dtype0*
value	B :S
q_dense_1/Pow_1/yConst*
_output_shapes
: *
dtype0*
value	B :o
q_dense_1/Pow_1Powq_dense_1/Pow_1/x:output:0q_dense_1/Pow_1/y:output:0*
T0*
_output_shapes
: ]
q_dense_1/Cast_1Castq_dense_1/Pow_1:z:0*

DstT0*

SrcT0*
_output_shapes
: z
q_dense_1/ReadVariableOp_3ReadVariableOp#q_dense_1_readvariableop_3_resource*
_output_shapes
:*
dtype0V
q_dense_1/mul_4/yConst*
_output_shapes
: *
dtype0*
valueB
 *  E{
q_dense_1/mul_4Mul"q_dense_1/ReadVariableOp_3:value:0q_dense_1/mul_4/y:output:0*
T0*
_output_shapes
:n
q_dense_1/truediv_2RealDivq_dense_1/mul_4:z:0q_dense_1/Cast_1:y:0*
T0*
_output_shapes
:T
q_dense_1/Neg_2Negq_dense_1/truediv_2:z:0*
T0*
_output_shapes
:X
q_dense_1/Round_1Roundq_dense_1/truediv_2:z:0*
T0*
_output_shapes
:i
q_dense_1/add_4AddV2q_dense_1/Neg_2:y:0q_dense_1/Round_1:y:0*
T0*
_output_shapes
:b
q_dense_1/StopGradient_2StopGradientq_dense_1/add_4:z:0*
T0*
_output_shapes
:y
q_dense_1/add_5AddV2q_dense_1/truediv_2:z:0!q_dense_1/StopGradient_2:output:0*
T0*
_output_shapes
:h
#q_dense_1/clip_by_value_1/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * πE
!q_dense_1/clip_by_value_1/MinimumMinimumq_dense_1/add_5:z:0,q_dense_1/clip_by_value_1/Minimum/y:output:0*
T0*
_output_shapes
:`
q_dense_1/clip_by_value_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *  Ε
q_dense_1/clip_by_value_1Maximum%q_dense_1/clip_by_value_1/Minimum:z:0$q_dense_1/clip_by_value_1/y:output:0*
T0*
_output_shapes
:p
q_dense_1/mul_5Mulq_dense_1/Cast_1:y:0q_dense_1/clip_by_value_1:z:0*
T0*
_output_shapes
:Z
q_dense_1/truediv_3/yConst*
_output_shapes
: *
dtype0*
valueB
 *  Ex
q_dense_1/truediv_3RealDivq_dense_1/mul_5:z:0q_dense_1/truediv_3/y:output:0*
T0*
_output_shapes
:V
q_dense_1/mul_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?p
q_dense_1/mul_6Mulq_dense_1/mul_6/x:output:0q_dense_1/truediv_3:z:0*
T0*
_output_shapes
:z
q_dense_1/ReadVariableOp_4ReadVariableOp#q_dense_1_readvariableop_3_resource*
_output_shapes
:*
dtype0_
q_dense_1/Neg_3Neg"q_dense_1/ReadVariableOp_4:value:0*
T0*
_output_shapes
:g
q_dense_1/add_6AddV2q_dense_1/Neg_3:y:0q_dense_1/mul_6:z:0*
T0*
_output_shapes
:V
q_dense_1/mul_7/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?l
q_dense_1/mul_7Mulq_dense_1/mul_7/x:output:0q_dense_1/add_6:z:0*
T0*
_output_shapes
:b
q_dense_1/StopGradient_3StopGradientq_dense_1/mul_7:z:0*
T0*
_output_shapes
:z
q_dense_1/ReadVariableOp_5ReadVariableOp#q_dense_1_readvariableop_3_resource*
_output_shapes
:*
dtype0
q_dense_1/add_7AddV2"q_dense_1/ReadVariableOp_5:value:0!q_dense_1/StopGradient_3:output:0*
T0*
_output_shapes
:
q_dense_1/BiasAddBiasAddq_dense_1/MatMul:product:0q_dense_1/add_7:z:0*
T0*'
_output_shapes
:?????????S
q_dense_1/Pow_2/xConst*
_output_shapes
: *
dtype0*
value	B :S
q_dense_1/Pow_2/yConst*
_output_shapes
: *
dtype0*
value	B :o
q_dense_1/Pow_2Powq_dense_1/Pow_2/x:output:0q_dense_1/Pow_2/y:output:0*
T0*
_output_shapes
: ]
q_dense_1/Cast_2Castq_dense_1/Pow_2:z:0*

DstT0*

SrcT0*
_output_shapes
: S
q_dense_1/Pow_3/xConst*
_output_shapes
: *
dtype0*
value	B :S
q_dense_1/Pow_3/yConst*
_output_shapes
: *
dtype0*
value	B :o
q_dense_1/Pow_3Powq_dense_1/Pow_3/x:output:0q_dense_1/Pow_3/y:output:0*
T0*
_output_shapes
: ]
q_dense_1/Cast_3Castq_dense_1/Pow_3:z:0*

DstT0*

SrcT0*
_output_shapes
: T
q_dense_1/ConstConst*
_output_shapes
: *
dtype0*
valueB
 *   @T
q_dense_1/Cast_4/xConst*
_output_shapes
: *
dtype0*
value	B :e
q_dense_1/Cast_4Castq_dense_1/Cast_4/x:output:0*

DstT0*

SrcT0*
_output_shapes
: T
q_dense_1/sub/yConst*
_output_shapes
: *
dtype0*
valueB
 *  PAe
q_dense_1/subSubq_dense_1/Cast_4:y:0q_dense_1/sub/y:output:0*
T0*
_output_shapes
: d
q_dense_1/Pow_4Powq_dense_1/Const:output:0q_dense_1/sub:z:0*
T0*
_output_shapes
: b
q_dense_1/sub_1Subq_dense_1/Cast_3:y:0q_dense_1/Pow_4:z:0*
T0*
_output_shapes
: 
q_dense_1/LessEqual	LessEqualq_dense_1/BiasAdd:output:0q_dense_1/sub_1:z:0*
T0*'
_output_shapes
:?????????d
q_dense_1/ReluReluq_dense_1/BiasAdd:output:0*
T0*'
_output_shapes
:?????????c
q_dense_1/ones_like/ShapeShapeq_dense_1/BiasAdd:output:0*
T0*
_output_shapes
:^
q_dense_1/ones_like/ConstConst*
_output_shapes
: *
dtype0*
valueB
 *  ?
q_dense_1/ones_likeFill"q_dense_1/ones_like/Shape:output:0"q_dense_1/ones_like/Const:output:0*
T0*'
_output_shapes
:?????????b
q_dense_1/sub_2Subq_dense_1/Cast_3:y:0q_dense_1/Pow_4:z:0*
T0*
_output_shapes
: {
q_dense_1/mul_8Mulq_dense_1/ones_like:output:0q_dense_1/sub_2:z:0*
T0*'
_output_shapes
:?????????
q_dense_1/SelectV2SelectV2q_dense_1/LessEqual:z:0q_dense_1/Relu:activations:0q_dense_1/mul_8:z:0*
T0*'
_output_shapes
:?????????z
q_dense_1/mul_9Mulq_dense_1/BiasAdd:output:0q_dense_1/Cast_2:y:0*
T0*'
_output_shapes
:?????????{
q_dense_1/truediv_4RealDivq_dense_1/mul_9:z:0q_dense_1/Cast_3:y:0*
T0*'
_output_shapes
:?????????a
q_dense_1/Neg_4Negq_dense_1/truediv_4:z:0*
T0*'
_output_shapes
:?????????e
q_dense_1/Round_2Roundq_dense_1/truediv_4:z:0*
T0*'
_output_shapes
:?????????v
q_dense_1/add_8AddV2q_dense_1/Neg_4:y:0q_dense_1/Round_2:y:0*
T0*'
_output_shapes
:?????????o
q_dense_1/StopGradient_4StopGradientq_dense_1/add_8:z:0*
T0*'
_output_shapes
:?????????
q_dense_1/add_9AddV2q_dense_1/truediv_4:z:0!q_dense_1/StopGradient_4:output:0*
T0*'
_output_shapes
:?????????{
q_dense_1/truediv_5RealDivq_dense_1/add_9:z:0q_dense_1/Cast_2:y:0*
T0*'
_output_shapes
:?????????Z
q_dense_1/truediv_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?u
q_dense_1/truediv_6RealDivq_dense_1/truediv_6/x:output:0q_dense_1/Cast_2:y:0*
T0*
_output_shapes
: V
q_dense_1/sub_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?l
q_dense_1/sub_3Subq_dense_1/sub_3/x:output:0q_dense_1/truediv_6:z:0*
T0*
_output_shapes
: 
!q_dense_1/clip_by_value_2/MinimumMinimumq_dense_1/truediv_5:z:0q_dense_1/sub_3:z:0*
T0*'
_output_shapes
:?????????`
q_dense_1/clip_by_value_2/yConst*
_output_shapes
: *
dtype0*
valueB
 *    £
q_dense_1/clip_by_value_2Maximum%q_dense_1/clip_by_value_2/Minimum:z:0$q_dense_1/clip_by_value_2/y:output:0*
T0*'
_output_shapes
:?????????~
q_dense_1/mul_10Mulq_dense_1/Cast_3:y:0q_dense_1/clip_by_value_2:z:0*
T0*'
_output_shapes
:?????????e
q_dense_1/Neg_5Negq_dense_1/SelectV2:output:0*
T0*'
_output_shapes
:?????????v
q_dense_1/add_10AddV2q_dense_1/Neg_5:y:0q_dense_1/mul_10:z:0*
T0*'
_output_shapes
:?????????W
q_dense_1/mul_11/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?|
q_dense_1/mul_11Mulq_dense_1/mul_11/x:output:0q_dense_1/add_10:z:0*
T0*'
_output_shapes
:?????????p
q_dense_1/StopGradient_5StopGradientq_dense_1/mul_11:z:0*
T0*'
_output_shapes
:?????????
q_dense_1/add_11AddV2q_dense_1/SelectV2:output:0!q_dense_1/StopGradient_5:output:0*
T0*'
_output_shapes
:?????????J
mu/Pow/xConst*
_output_shapes
: *
dtype0*
value	B :J
mu/Pow/yConst*
_output_shapes
: *
dtype0*
value	B :T
mu/PowPowmu/Pow/x:output:0mu/Pow/y:output:0*
T0*
_output_shapes
: K
mu/CastCast
mu/Pow:z:0*

DstT0*

SrcT0*
_output_shapes
: l
mu/ReadVariableOpReadVariableOpmu_readvariableop_resource*
_output_shapes

:*
dtype0M
mu/mul/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Bd
mu/mulMulmu/ReadVariableOp:value:0mu/mul/y:output:0*
T0*
_output_shapes

:W

mu/truedivRealDiv
mu/mul:z:0mu/Cast:y:0*
T0*
_output_shapes

:F
mu/NegNegmu/truediv:z:0*
T0*
_output_shapes

:J
mu/RoundRoundmu/truediv:z:0*
T0*
_output_shapes

:R
mu/addAddV2
mu/Neg:y:0mu/Round:y:0*
T0*
_output_shapes

:T
mu/StopGradientStopGradient
mu/add:z:0*
T0*
_output_shapes

:d
mu/add_1AddV2mu/truediv:z:0mu/StopGradient:output:0*
T0*
_output_shapes

:_
mu/clip_by_value/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 *  ψA
mu/clip_by_value/MinimumMinimummu/add_1:z:0#mu/clip_by_value/Minimum/y:output:0*
T0*
_output_shapes

:W
mu/clip_by_value/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Β
mu/clip_by_valueMaximummu/clip_by_value/Minimum:z:0mu/clip_by_value/y:output:0*
T0*
_output_shapes

:[
mu/mul_1Mulmu/Cast:y:0mu/clip_by_value:z:0*
T0*
_output_shapes

:S
mu/truediv_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Bg
mu/truediv_1RealDivmu/mul_1:z:0mu/truediv_1/y:output:0*
T0*
_output_shapes

:O

mu/mul_2/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?_
mu/mul_2Mulmu/mul_2/x:output:0mu/truediv_1:z:0*
T0*
_output_shapes

:n
mu/ReadVariableOp_1ReadVariableOpmu_readvariableop_resource*
_output_shapes

:*
dtype0U
mu/Neg_1Negmu/ReadVariableOp_1:value:0*
T0*
_output_shapes

:V
mu/add_2AddV2mu/Neg_1:y:0mu/mul_2:z:0*
T0*
_output_shapes

:O

mu/mul_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?[
mu/mul_3Mulmu/mul_3/x:output:0mu/add_2:z:0*
T0*
_output_shapes

:X
mu/StopGradient_1StopGradientmu/mul_3:z:0*
T0*
_output_shapes

:n
mu/ReadVariableOp_2ReadVariableOpmu_readvariableop_resource*
_output_shapes

:*
dtype0s
mu/add_3AddV2mu/ReadVariableOp_2:value:0mu/StopGradient_1:output:0*
T0*
_output_shapes

:i
	mu/MatMulMatMulq_dense_1/add_11:z:0mu/add_3:z:0*
T0*'
_output_shapes
:?????????L

mu/Pow_1/xConst*
_output_shapes
: *
dtype0*
value	B :L

mu/Pow_1/yConst*
_output_shapes
: *
dtype0*
value	B :Z
mu/Pow_1Powmu/Pow_1/x:output:0mu/Pow_1/y:output:0*
T0*
_output_shapes
: O
	mu/Cast_1Castmu/Pow_1:z:0*

DstT0*

SrcT0*
_output_shapes
: l
mu/ReadVariableOp_3ReadVariableOpmu_readvariableop_3_resource*
_output_shapes
:*
dtype0O

mu/mul_4/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Df
mu/mul_4Mulmu/ReadVariableOp_3:value:0mu/mul_4/y:output:0*
T0*
_output_shapes
:Y
mu/truediv_2RealDivmu/mul_4:z:0mu/Cast_1:y:0*
T0*
_output_shapes
:F
mu/Neg_2Negmu/truediv_2:z:0*
T0*
_output_shapes
:J

mu/Round_1Roundmu/truediv_2:z:0*
T0*
_output_shapes
:T
mu/add_4AddV2mu/Neg_2:y:0mu/Round_1:y:0*
T0*
_output_shapes
:T
mu/StopGradient_2StopGradientmu/add_4:z:0*
T0*
_output_shapes
:d
mu/add_5AddV2mu/truediv_2:z:0mu/StopGradient_2:output:0*
T0*
_output_shapes
:a
mu/clip_by_value_1/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * ?C
mu/clip_by_value_1/MinimumMinimummu/add_5:z:0%mu/clip_by_value_1/Minimum/y:output:0*
T0*
_output_shapes
:Y
mu/clip_by_value_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Δ
mu/clip_by_value_1Maximummu/clip_by_value_1/Minimum:z:0mu/clip_by_value_1/y:output:0*
T0*
_output_shapes
:[
mu/mul_5Mulmu/Cast_1:y:0mu/clip_by_value_1:z:0*
T0*
_output_shapes
:S
mu/truediv_3/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Dc
mu/truediv_3RealDivmu/mul_5:z:0mu/truediv_3/y:output:0*
T0*
_output_shapes
:O

mu/mul_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?[
mu/mul_6Mulmu/mul_6/x:output:0mu/truediv_3:z:0*
T0*
_output_shapes
:l
mu/ReadVariableOp_4ReadVariableOpmu_readvariableop_3_resource*
_output_shapes
:*
dtype0Q
mu/Neg_3Negmu/ReadVariableOp_4:value:0*
T0*
_output_shapes
:R
mu/add_6AddV2mu/Neg_3:y:0mu/mul_6:z:0*
T0*
_output_shapes
:O

mu/mul_7/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?W
mu/mul_7Mulmu/mul_7/x:output:0mu/add_6:z:0*
T0*
_output_shapes
:T
mu/StopGradient_3StopGradientmu/mul_7:z:0*
T0*
_output_shapes
:l
mu/ReadVariableOp_5ReadVariableOpmu_readvariableop_3_resource*
_output_shapes
:*
dtype0o
mu/add_7AddV2mu/ReadVariableOp_5:value:0mu/StopGradient_3:output:0*
T0*
_output_shapes
:j

mu/BiasAddBiasAddmu/MatMul:product:0mu/add_7:z:0*
T0*'
_output_shapes
:?????????L

mu/Pow_2/xConst*
_output_shapes
: *
dtype0*
value	B :L

mu/Pow_2/yConst*
_output_shapes
: *
dtype0*
value	B :Z
mu/Pow_2Powmu/Pow_2/x:output:0mu/Pow_2/y:output:0*
T0*
_output_shapes
: O
	mu/Cast_2Castmu/Pow_2:z:0*

DstT0*

SrcT0*
_output_shapes
: O

mu/mul_8/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Dk
mu/mul_8Mulmu/BiasAdd:output:0mu/mul_8/y:output:0*
T0*'
_output_shapes
:?????????f
mu/truediv_4RealDivmu/mul_8:z:0mu/Cast_2:y:0*
T0*'
_output_shapes
:?????????S
mu/Neg_4Negmu/truediv_4:z:0*
T0*'
_output_shapes
:?????????W

mu/Round_2Roundmu/truediv_4:z:0*
T0*'
_output_shapes
:?????????a
mu/add_8AddV2mu/Neg_4:y:0mu/Round_2:y:0*
T0*'
_output_shapes
:?????????a
mu/StopGradient_4StopGradientmu/add_8:z:0*
T0*'
_output_shapes
:?????????q
mu/add_9AddV2mu/truediv_4:z:0mu/StopGradient_4:output:0*
T0*'
_output_shapes
:?????????a
mu/clip_by_value_2/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * ?C
mu/clip_by_value_2/MinimumMinimummu/add_9:z:0%mu/clip_by_value_2/Minimum/y:output:0*
T0*'
_output_shapes
:?????????Y
mu/clip_by_value_2/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Δ
mu/clip_by_value_2Maximummu/clip_by_value_2/Minimum:z:0mu/clip_by_value_2/y:output:0*
T0*'
_output_shapes
:?????????h
mu/mul_9Mulmu/Cast_2:y:0mu/clip_by_value_2:z:0*
T0*'
_output_shapes
:?????????S
mu/truediv_5/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Dp
mu/truediv_5RealDivmu/mul_9:z:0mu/truediv_5/y:output:0*
T0*'
_output_shapes
:?????????P
mu/mul_10/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?j
	mu/mul_10Mulmu/mul_10/x:output:0mu/truediv_5:z:0*
T0*'
_output_shapes
:?????????V
mu/Neg_5Negmu/BiasAdd:output:0*
T0*'
_output_shapes
:?????????a
	mu/add_10AddV2mu/Neg_5:y:0mu/mul_10:z:0*
T0*'
_output_shapes
:?????????P
mu/mul_11/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?g
	mu/mul_11Mulmu/mul_11/x:output:0mu/add_10:z:0*
T0*'
_output_shapes
:?????????b
mu/StopGradient_5StopGradientmu/mul_11:z:0*
T0*'
_output_shapes
:?????????u
	mu/add_11AddV2mu/BiasAdd:output:0mu/StopGradient_5:output:0*
T0*'
_output_shapes
:?????????
-q_dense/kernel/Regularizer/Abs/ReadVariableOpReadVariableOpq_dense_readvariableop_resource*
_output_shapes

:9 *
dtype0
q_dense/kernel/Regularizer/AbsAbs5q_dense/kernel/Regularizer/Abs/ReadVariableOp:value:0*
T0*
_output_shapes

:9 q
 q_dense/kernel/Regularizer/ConstConst*
_output_shapes
:*
dtype0*
valueB"       
q_dense/kernel/Regularizer/SumSum"q_dense/kernel/Regularizer/Abs:y:0)q_dense/kernel/Regularizer/Const:output:0*
T0*
_output_shapes
: e
 q_dense/kernel/Regularizer/mul/xConst*
_output_shapes
: *
dtype0*
valueB
 *o:
q_dense/kernel/Regularizer/mulMul)q_dense/kernel/Regularizer/mul/x:output:0'q_dense/kernel/Regularizer/Sum:output:0*
T0*
_output_shapes
: 
/q_dense_1/kernel/Regularizer/Abs/ReadVariableOpReadVariableOp!q_dense_1_readvariableop_resource*
_output_shapes

: *
dtype0
 q_dense_1/kernel/Regularizer/AbsAbs7q_dense_1/kernel/Regularizer/Abs/ReadVariableOp:value:0*
T0*
_output_shapes

: s
"q_dense_1/kernel/Regularizer/ConstConst*
_output_shapes
:*
dtype0*
valueB"       
 q_dense_1/kernel/Regularizer/SumSum$q_dense_1/kernel/Regularizer/Abs:y:0+q_dense_1/kernel/Regularizer/Const:output:0*
T0*
_output_shapes
: g
"q_dense_1/kernel/Regularizer/mul/xConst*
_output_shapes
: *
dtype0*
valueB
 *     
 q_dense_1/kernel/Regularizer/mulMul+q_dense_1/kernel/Regularizer/mul/x:output:0)q_dense_1/kernel/Regularizer/Sum:output:0*
T0*
_output_shapes
: \
IdentityIdentitymu/add_11:z:0^NoOp*
T0*'
_output_shapes
:?????????φ
NoOpNoOp^mu/ReadVariableOp^mu/ReadVariableOp_1^mu/ReadVariableOp_2^mu/ReadVariableOp_3^mu/ReadVariableOp_4^mu/ReadVariableOp_5^q_dense/ReadVariableOp^q_dense/ReadVariableOp_1^q_dense/ReadVariableOp_2^q_dense/ReadVariableOp_3^q_dense/ReadVariableOp_4^q_dense/ReadVariableOp_5.^q_dense/kernel/Regularizer/Abs/ReadVariableOp^q_dense_1/ReadVariableOp^q_dense_1/ReadVariableOp_1^q_dense_1/ReadVariableOp_2^q_dense_1/ReadVariableOp_3^q_dense_1/ReadVariableOp_4^q_dense_1/ReadVariableOp_50^q_dense_1/kernel/Regularizer/Abs/ReadVariableOp*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*2
_input_shapes!
:?????????9: : : : : : 2&
mu/ReadVariableOpmu/ReadVariableOp2*
mu/ReadVariableOp_1mu/ReadVariableOp_12*
mu/ReadVariableOp_2mu/ReadVariableOp_22*
mu/ReadVariableOp_3mu/ReadVariableOp_32*
mu/ReadVariableOp_4mu/ReadVariableOp_42*
mu/ReadVariableOp_5mu/ReadVariableOp_520
q_dense/ReadVariableOpq_dense/ReadVariableOp24
q_dense/ReadVariableOp_1q_dense/ReadVariableOp_124
q_dense/ReadVariableOp_2q_dense/ReadVariableOp_224
q_dense/ReadVariableOp_3q_dense/ReadVariableOp_324
q_dense/ReadVariableOp_4q_dense/ReadVariableOp_424
q_dense/ReadVariableOp_5q_dense/ReadVariableOp_52^
-q_dense/kernel/Regularizer/Abs/ReadVariableOp-q_dense/kernel/Regularizer/Abs/ReadVariableOp24
q_dense_1/ReadVariableOpq_dense_1/ReadVariableOp28
q_dense_1/ReadVariableOp_1q_dense_1/ReadVariableOp_128
q_dense_1/ReadVariableOp_2q_dense_1/ReadVariableOp_228
q_dense_1/ReadVariableOp_3q_dense_1/ReadVariableOp_328
q_dense_1/ReadVariableOp_4q_dense_1/ReadVariableOp_428
q_dense_1/ReadVariableOp_5q_dense_1/ReadVariableOp_52b
/q_dense_1/kernel/Regularizer/Abs/ReadVariableOp/q_dense_1/kernel/Regularizer/Abs/ReadVariableOp:O K
'
_output_shapes
:?????????9
 
_user_specified_nameinputs
 
G
+__inference_q_activation_layer_call_fn_2163

inputs
identity°
PartitionedCallPartitionedCallinputs*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????9* 
_read_only_resource_inputs
 *-
config_proto

CPU

GPU 2J 8 *N
fIRG
E__inference_q_activation_layer_call_and_return_conditional_losses_813`
IdentityIdentityPartitionedCall:output:0*
T0*'
_output_shapes
:?????????9"
identityIdentity:output:0*(
_construction_contextkEagerRuntime*&
_input_shapes
:?????????9:O K
'
_output_shapes
:?????????9
 
_user_specified_nameinputs
ΰ
ύ
$__inference_model_layer_call_fn_1437

inputs
unknown:9 
	unknown_0: 
	unknown_1: 
	unknown_2:
	unknown_3:
	unknown_4:
identity’StatefulPartitionedCall
StatefulPartitionedCallStatefulPartitionedCallinputsunknown	unknown_0	unknown_1	unknown_2	unknown_3	unknown_4*
Tin
	2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*(
_read_only_resource_inputs

*-
config_proto

CPU

GPU 2J 8 *H
fCRA
?__inference_model_layer_call_and_return_conditional_losses_1179o
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*'
_output_shapes
:?????????`
NoOpNoOp^StatefulPartitionedCall*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*2
_input_shapes!
:?????????9: : : : : : 22
StatefulPartitionedCallStatefulPartitionedCall:O K
'
_output_shapes
:?????????9
 
_user_specified_nameinputs
ΌX
Σ
@__inference_q_dense_layer_call_and_return_conditional_losses_934

inputs)
readvariableop_resource:9 '
readvariableop_3_resource: 
identity’ReadVariableOp’ReadVariableOp_1’ReadVariableOp_2’ReadVariableOp_3’ReadVariableOp_4’ReadVariableOp_5’-q_dense/kernel/Regularizer/Abs/ReadVariableOpG
Pow/xConst*
_output_shapes
: *
dtype0*
value	B :G
Pow/yConst*
_output_shapes
: *
dtype0*
value	B :K
PowPowPow/x:output:0Pow/y:output:0*
T0*
_output_shapes
: E
CastCastPow:z:0*

DstT0*

SrcT0*
_output_shapes
: f
ReadVariableOpReadVariableOpreadvariableop_resource*
_output_shapes

:9 *
dtype0J
mul/yConst*
_output_shapes
: *
dtype0*
valueB
 *   B[
mulMulReadVariableOp:value:0mul/y:output:0*
T0*
_output_shapes

:9 N
truedivRealDivmul:z:0Cast:y:0*
T0*
_output_shapes

:9 @
NegNegtruediv:z:0*
T0*
_output_shapes

:9 D
RoundRoundtruediv:z:0*
T0*
_output_shapes

:9 I
addAddV2Neg:y:0	Round:y:0*
T0*
_output_shapes

:9 N
StopGradientStopGradientadd:z:0*
T0*
_output_shapes

:9 [
add_1AddV2truediv:z:0StopGradient:output:0*
T0*
_output_shapes

:9 \
clip_by_value/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 *  ψAv
clip_by_value/MinimumMinimum	add_1:z:0 clip_by_value/Minimum/y:output:0*
T0*
_output_shapes

:9 T
clip_by_value/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Βv
clip_by_valueMaximumclip_by_value/Minimum:z:0clip_by_value/y:output:0*
T0*
_output_shapes

:9 R
mul_1MulCast:y:0clip_by_value:z:0*
T0*
_output_shapes

:9 P
truediv_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   B^
	truediv_1RealDiv	mul_1:z:0truediv_1/y:output:0*
T0*
_output_shapes

:9 L
mul_2/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?V
mul_2Mulmul_2/x:output:0truediv_1:z:0*
T0*
_output_shapes

:9 h
ReadVariableOp_1ReadVariableOpreadvariableop_resource*
_output_shapes

:9 *
dtype0O
Neg_1NegReadVariableOp_1:value:0*
T0*
_output_shapes

:9 M
add_2AddV2	Neg_1:y:0	mul_2:z:0*
T0*
_output_shapes

:9 L
mul_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?R
mul_3Mulmul_3/x:output:0	add_2:z:0*
T0*
_output_shapes

:9 R
StopGradient_1StopGradient	mul_3:z:0*
T0*
_output_shapes

:9 h
ReadVariableOp_2ReadVariableOpreadvariableop_resource*
_output_shapes

:9 *
dtype0j
add_3AddV2ReadVariableOp_2:value:0StopGradient_1:output:0*
T0*
_output_shapes

:9 U
MatMulMatMulinputs	add_3:z:0*
T0*'
_output_shapes
:????????? I
Pow_1/xConst*
_output_shapes
: *
dtype0*
value	B :I
Pow_1/yConst*
_output_shapes
: *
dtype0*
value	B :Q
Pow_1PowPow_1/x:output:0Pow_1/y:output:0*
T0*
_output_shapes
: I
Cast_1Cast	Pow_1:z:0*

DstT0*

SrcT0*
_output_shapes
: f
ReadVariableOp_3ReadVariableOpreadvariableop_3_resource*
_output_shapes
: *
dtype0L
mul_4/yConst*
_output_shapes
: *
dtype0*
valueB
 *  E]
mul_4MulReadVariableOp_3:value:0mul_4/y:output:0*
T0*
_output_shapes
: P
	truediv_2RealDiv	mul_4:z:0
Cast_1:y:0*
T0*
_output_shapes
: @
Neg_2Negtruediv_2:z:0*
T0*
_output_shapes
: D
Round_1Roundtruediv_2:z:0*
T0*
_output_shapes
: K
add_4AddV2	Neg_2:y:0Round_1:y:0*
T0*
_output_shapes
: N
StopGradient_2StopGradient	add_4:z:0*
T0*
_output_shapes
: [
add_5AddV2truediv_2:z:0StopGradient_2:output:0*
T0*
_output_shapes
: ^
clip_by_value_1/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * πEv
clip_by_value_1/MinimumMinimum	add_5:z:0"clip_by_value_1/Minimum/y:output:0*
T0*
_output_shapes
: V
clip_by_value_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *  Εx
clip_by_value_1Maximumclip_by_value_1/Minimum:z:0clip_by_value_1/y:output:0*
T0*
_output_shapes
: R
mul_5Mul
Cast_1:y:0clip_by_value_1:z:0*
T0*
_output_shapes
: P
truediv_3/yConst*
_output_shapes
: *
dtype0*
valueB
 *  EZ
	truediv_3RealDiv	mul_5:z:0truediv_3/y:output:0*
T0*
_output_shapes
: L
mul_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?R
mul_6Mulmul_6/x:output:0truediv_3:z:0*
T0*
_output_shapes
: f
ReadVariableOp_4ReadVariableOpreadvariableop_3_resource*
_output_shapes
: *
dtype0K
Neg_3NegReadVariableOp_4:value:0*
T0*
_output_shapes
: I
add_6AddV2	Neg_3:y:0	mul_6:z:0*
T0*
_output_shapes
: L
mul_7/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?N
mul_7Mulmul_7/x:output:0	add_6:z:0*
T0*
_output_shapes
: N
StopGradient_3StopGradient	mul_7:z:0*
T0*
_output_shapes
: f
ReadVariableOp_5ReadVariableOpreadvariableop_3_resource*
_output_shapes
: *
dtype0f
add_7AddV2ReadVariableOp_5:value:0StopGradient_3:output:0*
T0*
_output_shapes
: a
BiasAddBiasAddMatMul:product:0	add_7:z:0*
T0*'
_output_shapes
:????????? I
Pow_2/xConst*
_output_shapes
: *
dtype0*
value	B :I
Pow_2/yConst*
_output_shapes
: *
dtype0*
value	B :Q
Pow_2PowPow_2/x:output:0Pow_2/y:output:0*
T0*
_output_shapes
: I
Cast_2Cast	Pow_2:z:0*

DstT0*

SrcT0*
_output_shapes
: I
Pow_3/xConst*
_output_shapes
: *
dtype0*
value	B :I
Pow_3/yConst*
_output_shapes
: *
dtype0*
value	B :Q
Pow_3PowPow_3/x:output:0Pow_3/y:output:0*
T0*
_output_shapes
: I
Cast_3Cast	Pow_3:z:0*

DstT0*

SrcT0*
_output_shapes
: J
ConstConst*
_output_shapes
: *
dtype0*
valueB
 *   @J
Cast_4/xConst*
_output_shapes
: *
dtype0*
value	B :Q
Cast_4CastCast_4/x:output:0*

DstT0*

SrcT0*
_output_shapes
: J
sub/yConst*
_output_shapes
: *
dtype0*
valueB
 *  PAG
subSub
Cast_4:y:0sub/y:output:0*
T0*
_output_shapes
: F
Pow_4PowConst:output:0sub:z:0*
T0*
_output_shapes
: D
sub_1Sub
Cast_3:y:0	Pow_4:z:0*
T0*
_output_shapes
: e
	LessEqual	LessEqualBiasAdd:output:0	sub_1:z:0*
T0*'
_output_shapes
:????????? P
ReluReluBiasAdd:output:0*
T0*'
_output_shapes
:????????? O
ones_like/ShapeShapeBiasAdd:output:0*
T0*
_output_shapes
:T
ones_like/ConstConst*
_output_shapes
: *
dtype0*
valueB
 *  ?w
	ones_likeFillones_like/Shape:output:0ones_like/Const:output:0*
T0*'
_output_shapes
:????????? D
sub_2Sub
Cast_3:y:0	Pow_4:z:0*
T0*
_output_shapes
: ]
mul_8Mulones_like:output:0	sub_2:z:0*
T0*'
_output_shapes
:????????? t
SelectV2SelectV2LessEqual:z:0Relu:activations:0	mul_8:z:0*
T0*'
_output_shapes
:????????? \
mul_9MulBiasAdd:output:0
Cast_2:y:0*
T0*'
_output_shapes
:????????? ]
	truediv_4RealDiv	mul_9:z:0
Cast_3:y:0*
T0*'
_output_shapes
:????????? M
Neg_4Negtruediv_4:z:0*
T0*'
_output_shapes
:????????? Q
Round_2Roundtruediv_4:z:0*
T0*'
_output_shapes
:????????? X
add_8AddV2	Neg_4:y:0Round_2:y:0*
T0*'
_output_shapes
:????????? [
StopGradient_4StopGradient	add_8:z:0*
T0*'
_output_shapes
:????????? h
add_9AddV2truediv_4:z:0StopGradient_4:output:0*
T0*'
_output_shapes
:????????? ]
	truediv_5RealDiv	add_9:z:0
Cast_2:y:0*
T0*'
_output_shapes
:????????? P
truediv_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?W
	truediv_6RealDivtruediv_6/x:output:0
Cast_2:y:0*
T0*
_output_shapes
: L
sub_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?N
sub_3Subsub_3/x:output:0truediv_6:z:0*
T0*
_output_shapes
: n
clip_by_value_2/MinimumMinimumtruediv_5:z:0	sub_3:z:0*
T0*'
_output_shapes
:????????? V
clip_by_value_2/yConst*
_output_shapes
: *
dtype0*
valueB
 *    
clip_by_value_2Maximumclip_by_value_2/Minimum:z:0clip_by_value_2/y:output:0*
T0*'
_output_shapes
:????????? `
mul_10Mul
Cast_3:y:0clip_by_value_2:z:0*
T0*'
_output_shapes
:????????? Q
Neg_5NegSelectV2:output:0*
T0*'
_output_shapes
:????????? X
add_10AddV2	Neg_5:y:0
mul_10:z:0*
T0*'
_output_shapes
:????????? M
mul_11/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?^
mul_11Mulmul_11/x:output:0
add_10:z:0*
T0*'
_output_shapes
:????????? \
StopGradient_5StopGradient
mul_11:z:0*
T0*'
_output_shapes
:????????? m
add_11AddV2SelectV2:output:0StopGradient_5:output:0*
T0*'
_output_shapes
:????????? 
-q_dense/kernel/Regularizer/Abs/ReadVariableOpReadVariableOpreadvariableop_resource*
_output_shapes

:9 *
dtype0
q_dense/kernel/Regularizer/AbsAbs5q_dense/kernel/Regularizer/Abs/ReadVariableOp:value:0*
T0*
_output_shapes

:9 q
 q_dense/kernel/Regularizer/ConstConst*
_output_shapes
:*
dtype0*
valueB"       
q_dense/kernel/Regularizer/SumSum"q_dense/kernel/Regularizer/Abs:y:0)q_dense/kernel/Regularizer/Const:output:0*
T0*
_output_shapes
: e
 q_dense/kernel/Regularizer/mul/xConst*
_output_shapes
: *
dtype0*
valueB
 *o:
q_dense/kernel/Regularizer/mulMul)q_dense/kernel/Regularizer/mul/x:output:0'q_dense/kernel/Regularizer/Sum:output:0*
T0*
_output_shapes
: Y
IdentityIdentity
add_11:z:0^NoOp*
T0*'
_output_shapes
:????????? ζ
NoOpNoOp^ReadVariableOp^ReadVariableOp_1^ReadVariableOp_2^ReadVariableOp_3^ReadVariableOp_4^ReadVariableOp_5.^q_dense/kernel/Regularizer/Abs/ReadVariableOp*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime**
_input_shapes
:?????????9: : 2 
ReadVariableOpReadVariableOp2$
ReadVariableOp_1ReadVariableOp_12$
ReadVariableOp_2ReadVariableOp_22$
ReadVariableOp_3ReadVariableOp_32$
ReadVariableOp_4ReadVariableOp_42$
ReadVariableOp_5ReadVariableOp_52^
-q_dense/kernel/Regularizer/Abs/ReadVariableOp-q_dense/kernel/Regularizer/Abs/ReadVariableOp:O K
'
_output_shapes
:?????????9
 
_user_specified_nameinputs
ΰ
ύ
$__inference_model_layer_call_fn_1454

inputs
unknown:9 
	unknown_0: 
	unknown_1: 
	unknown_2:
	unknown_3:
	unknown_4:
identity’StatefulPartitionedCall
StatefulPartitionedCallStatefulPartitionedCallinputsunknown	unknown_0	unknown_1	unknown_2	unknown_3	unknown_4*
Tin
	2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*(
_read_only_resource_inputs

*-
config_proto

CPU

GPU 2J 8 *H
fCRA
?__inference_model_layer_call_and_return_conditional_losses_1281o
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*'
_output_shapes
:?????????`
NoOpNoOp^StatefulPartitionedCall*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*2
_input_shapes!
:?????????9: : : : : : 22
StatefulPartitionedCallStatefulPartitionedCall:O K
'
_output_shapes
:?????????9
 
_user_specified_nameinputs
Β#
?
?__inference_model_layer_call_and_return_conditional_losses_1345
input_1
q_dense_1317:9 
q_dense_1319:  
q_dense_1_1322: 
q_dense_1_1324:
mu_1327:
mu_1329:
identity’mu/StatefulPartitionedCall’q_dense/StatefulPartitionedCall’-q_dense/kernel/Regularizer/Abs/ReadVariableOp’!q_dense_1/StatefulPartitionedCall’/q_dense_1/kernel/Regularizer/Abs/ReadVariableOpΎ
q_activation/PartitionedCallPartitionedCallinput_1*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????9* 
_read_only_resource_inputs
 *-
config_proto

CPU

GPU 2J 8 *N
fIRG
E__inference_q_activation_layer_call_and_return_conditional_losses_813
q_dense/StatefulPartitionedCallStatefulPartitionedCall%q_activation/PartitionedCall:output:0q_dense_1317q_dense_1319*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:????????? *$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8 *I
fDRB
@__inference_q_dense_layer_call_and_return_conditional_losses_934
!q_dense_1/StatefulPartitionedCallStatefulPartitionedCall(q_dense/StatefulPartitionedCall:output:0q_dense_1_1322q_dense_1_1324*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8 *L
fGRE
C__inference_q_dense_1_layer_call_and_return_conditional_losses_1059φ
mu/StatefulPartitionedCallStatefulPartitionedCall*q_dense_1/StatefulPartitionedCall:output:0mu_1327mu_1329*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8 *E
f@R>
<__inference_mu_layer_call_and_return_conditional_losses_1160z
-q_dense/kernel/Regularizer/Abs/ReadVariableOpReadVariableOpq_dense_1317*
_output_shapes

:9 *
dtype0
q_dense/kernel/Regularizer/AbsAbs5q_dense/kernel/Regularizer/Abs/ReadVariableOp:value:0*
T0*
_output_shapes

:9 q
 q_dense/kernel/Regularizer/ConstConst*
_output_shapes
:*
dtype0*
valueB"       
q_dense/kernel/Regularizer/SumSum"q_dense/kernel/Regularizer/Abs:y:0)q_dense/kernel/Regularizer/Const:output:0*
T0*
_output_shapes
: e
 q_dense/kernel/Regularizer/mul/xConst*
_output_shapes
: *
dtype0*
valueB
 *o:
q_dense/kernel/Regularizer/mulMul)q_dense/kernel/Regularizer/mul/x:output:0'q_dense/kernel/Regularizer/Sum:output:0*
T0*
_output_shapes
: ~
/q_dense_1/kernel/Regularizer/Abs/ReadVariableOpReadVariableOpq_dense_1_1322*
_output_shapes

: *
dtype0
 q_dense_1/kernel/Regularizer/AbsAbs7q_dense_1/kernel/Regularizer/Abs/ReadVariableOp:value:0*
T0*
_output_shapes

: s
"q_dense_1/kernel/Regularizer/ConstConst*
_output_shapes
:*
dtype0*
valueB"       
 q_dense_1/kernel/Regularizer/SumSum$q_dense_1/kernel/Regularizer/Abs:y:0+q_dense_1/kernel/Regularizer/Const:output:0*
T0*
_output_shapes
: g
"q_dense_1/kernel/Regularizer/mul/xConst*
_output_shapes
: *
dtype0*
valueB
 *     
 q_dense_1/kernel/Regularizer/mulMul+q_dense_1/kernel/Regularizer/mul/x:output:0)q_dense_1/kernel/Regularizer/Sum:output:0*
T0*
_output_shapes
: r
IdentityIdentity#mu/StatefulPartitionedCall:output:0^NoOp*
T0*'
_output_shapes
:?????????
NoOpNoOp^mu/StatefulPartitionedCall ^q_dense/StatefulPartitionedCall.^q_dense/kernel/Regularizer/Abs/ReadVariableOp"^q_dense_1/StatefulPartitionedCall0^q_dense_1/kernel/Regularizer/Abs/ReadVariableOp*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*2
_input_shapes!
:?????????9: : : : : : 28
mu/StatefulPartitionedCallmu/StatefulPartitionedCall2B
q_dense/StatefulPartitionedCallq_dense/StatefulPartitionedCall2^
-q_dense/kernel/Regularizer/Abs/ReadVariableOp-q_dense/kernel/Regularizer/Abs/ReadVariableOp2F
!q_dense_1/StatefulPartitionedCall!q_dense_1/StatefulPartitionedCall2b
/q_dense_1/kernel/Regularizer/Abs/ReadVariableOp/q_dense_1/kernel/Regularizer/Abs/ReadVariableOp:P L
'
_output_shapes
:?????????9
!
_user_specified_name	input_1
½X
Τ
A__inference_q_dense_layer_call_and_return_conditional_losses_2322

inputs)
readvariableop_resource:9 '
readvariableop_3_resource: 
identity’ReadVariableOp’ReadVariableOp_1’ReadVariableOp_2’ReadVariableOp_3’ReadVariableOp_4’ReadVariableOp_5’-q_dense/kernel/Regularizer/Abs/ReadVariableOpG
Pow/xConst*
_output_shapes
: *
dtype0*
value	B :G
Pow/yConst*
_output_shapes
: *
dtype0*
value	B :K
PowPowPow/x:output:0Pow/y:output:0*
T0*
_output_shapes
: E
CastCastPow:z:0*

DstT0*

SrcT0*
_output_shapes
: f
ReadVariableOpReadVariableOpreadvariableop_resource*
_output_shapes

:9 *
dtype0J
mul/yConst*
_output_shapes
: *
dtype0*
valueB
 *   B[
mulMulReadVariableOp:value:0mul/y:output:0*
T0*
_output_shapes

:9 N
truedivRealDivmul:z:0Cast:y:0*
T0*
_output_shapes

:9 @
NegNegtruediv:z:0*
T0*
_output_shapes

:9 D
RoundRoundtruediv:z:0*
T0*
_output_shapes

:9 I
addAddV2Neg:y:0	Round:y:0*
T0*
_output_shapes

:9 N
StopGradientStopGradientadd:z:0*
T0*
_output_shapes

:9 [
add_1AddV2truediv:z:0StopGradient:output:0*
T0*
_output_shapes

:9 \
clip_by_value/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 *  ψAv
clip_by_value/MinimumMinimum	add_1:z:0 clip_by_value/Minimum/y:output:0*
T0*
_output_shapes

:9 T
clip_by_value/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Βv
clip_by_valueMaximumclip_by_value/Minimum:z:0clip_by_value/y:output:0*
T0*
_output_shapes

:9 R
mul_1MulCast:y:0clip_by_value:z:0*
T0*
_output_shapes

:9 P
truediv_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   B^
	truediv_1RealDiv	mul_1:z:0truediv_1/y:output:0*
T0*
_output_shapes

:9 L
mul_2/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?V
mul_2Mulmul_2/x:output:0truediv_1:z:0*
T0*
_output_shapes

:9 h
ReadVariableOp_1ReadVariableOpreadvariableop_resource*
_output_shapes

:9 *
dtype0O
Neg_1NegReadVariableOp_1:value:0*
T0*
_output_shapes

:9 M
add_2AddV2	Neg_1:y:0	mul_2:z:0*
T0*
_output_shapes

:9 L
mul_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?R
mul_3Mulmul_3/x:output:0	add_2:z:0*
T0*
_output_shapes

:9 R
StopGradient_1StopGradient	mul_3:z:0*
T0*
_output_shapes

:9 h
ReadVariableOp_2ReadVariableOpreadvariableop_resource*
_output_shapes

:9 *
dtype0j
add_3AddV2ReadVariableOp_2:value:0StopGradient_1:output:0*
T0*
_output_shapes

:9 U
MatMulMatMulinputs	add_3:z:0*
T0*'
_output_shapes
:????????? I
Pow_1/xConst*
_output_shapes
: *
dtype0*
value	B :I
Pow_1/yConst*
_output_shapes
: *
dtype0*
value	B :Q
Pow_1PowPow_1/x:output:0Pow_1/y:output:0*
T0*
_output_shapes
: I
Cast_1Cast	Pow_1:z:0*

DstT0*

SrcT0*
_output_shapes
: f
ReadVariableOp_3ReadVariableOpreadvariableop_3_resource*
_output_shapes
: *
dtype0L
mul_4/yConst*
_output_shapes
: *
dtype0*
valueB
 *  E]
mul_4MulReadVariableOp_3:value:0mul_4/y:output:0*
T0*
_output_shapes
: P
	truediv_2RealDiv	mul_4:z:0
Cast_1:y:0*
T0*
_output_shapes
: @
Neg_2Negtruediv_2:z:0*
T0*
_output_shapes
: D
Round_1Roundtruediv_2:z:0*
T0*
_output_shapes
: K
add_4AddV2	Neg_2:y:0Round_1:y:0*
T0*
_output_shapes
: N
StopGradient_2StopGradient	add_4:z:0*
T0*
_output_shapes
: [
add_5AddV2truediv_2:z:0StopGradient_2:output:0*
T0*
_output_shapes
: ^
clip_by_value_1/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * πEv
clip_by_value_1/MinimumMinimum	add_5:z:0"clip_by_value_1/Minimum/y:output:0*
T0*
_output_shapes
: V
clip_by_value_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *  Εx
clip_by_value_1Maximumclip_by_value_1/Minimum:z:0clip_by_value_1/y:output:0*
T0*
_output_shapes
: R
mul_5Mul
Cast_1:y:0clip_by_value_1:z:0*
T0*
_output_shapes
: P
truediv_3/yConst*
_output_shapes
: *
dtype0*
valueB
 *  EZ
	truediv_3RealDiv	mul_5:z:0truediv_3/y:output:0*
T0*
_output_shapes
: L
mul_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?R
mul_6Mulmul_6/x:output:0truediv_3:z:0*
T0*
_output_shapes
: f
ReadVariableOp_4ReadVariableOpreadvariableop_3_resource*
_output_shapes
: *
dtype0K
Neg_3NegReadVariableOp_4:value:0*
T0*
_output_shapes
: I
add_6AddV2	Neg_3:y:0	mul_6:z:0*
T0*
_output_shapes
: L
mul_7/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?N
mul_7Mulmul_7/x:output:0	add_6:z:0*
T0*
_output_shapes
: N
StopGradient_3StopGradient	mul_7:z:0*
T0*
_output_shapes
: f
ReadVariableOp_5ReadVariableOpreadvariableop_3_resource*
_output_shapes
: *
dtype0f
add_7AddV2ReadVariableOp_5:value:0StopGradient_3:output:0*
T0*
_output_shapes
: a
BiasAddBiasAddMatMul:product:0	add_7:z:0*
T0*'
_output_shapes
:????????? I
Pow_2/xConst*
_output_shapes
: *
dtype0*
value	B :I
Pow_2/yConst*
_output_shapes
: *
dtype0*
value	B :Q
Pow_2PowPow_2/x:output:0Pow_2/y:output:0*
T0*
_output_shapes
: I
Cast_2Cast	Pow_2:z:0*

DstT0*

SrcT0*
_output_shapes
: I
Pow_3/xConst*
_output_shapes
: *
dtype0*
value	B :I
Pow_3/yConst*
_output_shapes
: *
dtype0*
value	B :Q
Pow_3PowPow_3/x:output:0Pow_3/y:output:0*
T0*
_output_shapes
: I
Cast_3Cast	Pow_3:z:0*

DstT0*

SrcT0*
_output_shapes
: J
ConstConst*
_output_shapes
: *
dtype0*
valueB
 *   @J
Cast_4/xConst*
_output_shapes
: *
dtype0*
value	B :Q
Cast_4CastCast_4/x:output:0*

DstT0*

SrcT0*
_output_shapes
: J
sub/yConst*
_output_shapes
: *
dtype0*
valueB
 *  PAG
subSub
Cast_4:y:0sub/y:output:0*
T0*
_output_shapes
: F
Pow_4PowConst:output:0sub:z:0*
T0*
_output_shapes
: D
sub_1Sub
Cast_3:y:0	Pow_4:z:0*
T0*
_output_shapes
: e
	LessEqual	LessEqualBiasAdd:output:0	sub_1:z:0*
T0*'
_output_shapes
:????????? P
ReluReluBiasAdd:output:0*
T0*'
_output_shapes
:????????? O
ones_like/ShapeShapeBiasAdd:output:0*
T0*
_output_shapes
:T
ones_like/ConstConst*
_output_shapes
: *
dtype0*
valueB
 *  ?w
	ones_likeFillones_like/Shape:output:0ones_like/Const:output:0*
T0*'
_output_shapes
:????????? D
sub_2Sub
Cast_3:y:0	Pow_4:z:0*
T0*
_output_shapes
: ]
mul_8Mulones_like:output:0	sub_2:z:0*
T0*'
_output_shapes
:????????? t
SelectV2SelectV2LessEqual:z:0Relu:activations:0	mul_8:z:0*
T0*'
_output_shapes
:????????? \
mul_9MulBiasAdd:output:0
Cast_2:y:0*
T0*'
_output_shapes
:????????? ]
	truediv_4RealDiv	mul_9:z:0
Cast_3:y:0*
T0*'
_output_shapes
:????????? M
Neg_4Negtruediv_4:z:0*
T0*'
_output_shapes
:????????? Q
Round_2Roundtruediv_4:z:0*
T0*'
_output_shapes
:????????? X
add_8AddV2	Neg_4:y:0Round_2:y:0*
T0*'
_output_shapes
:????????? [
StopGradient_4StopGradient	add_8:z:0*
T0*'
_output_shapes
:????????? h
add_9AddV2truediv_4:z:0StopGradient_4:output:0*
T0*'
_output_shapes
:????????? ]
	truediv_5RealDiv	add_9:z:0
Cast_2:y:0*
T0*'
_output_shapes
:????????? P
truediv_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?W
	truediv_6RealDivtruediv_6/x:output:0
Cast_2:y:0*
T0*
_output_shapes
: L
sub_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?N
sub_3Subsub_3/x:output:0truediv_6:z:0*
T0*
_output_shapes
: n
clip_by_value_2/MinimumMinimumtruediv_5:z:0	sub_3:z:0*
T0*'
_output_shapes
:????????? V
clip_by_value_2/yConst*
_output_shapes
: *
dtype0*
valueB
 *    
clip_by_value_2Maximumclip_by_value_2/Minimum:z:0clip_by_value_2/y:output:0*
T0*'
_output_shapes
:????????? `
mul_10Mul
Cast_3:y:0clip_by_value_2:z:0*
T0*'
_output_shapes
:????????? Q
Neg_5NegSelectV2:output:0*
T0*'
_output_shapes
:????????? X
add_10AddV2	Neg_5:y:0
mul_10:z:0*
T0*'
_output_shapes
:????????? M
mul_11/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?^
mul_11Mulmul_11/x:output:0
add_10:z:0*
T0*'
_output_shapes
:????????? \
StopGradient_5StopGradient
mul_11:z:0*
T0*'
_output_shapes
:????????? m
add_11AddV2SelectV2:output:0StopGradient_5:output:0*
T0*'
_output_shapes
:????????? 
-q_dense/kernel/Regularizer/Abs/ReadVariableOpReadVariableOpreadvariableop_resource*
_output_shapes

:9 *
dtype0
q_dense/kernel/Regularizer/AbsAbs5q_dense/kernel/Regularizer/Abs/ReadVariableOp:value:0*
T0*
_output_shapes

:9 q
 q_dense/kernel/Regularizer/ConstConst*
_output_shapes
:*
dtype0*
valueB"       
q_dense/kernel/Regularizer/SumSum"q_dense/kernel/Regularizer/Abs:y:0)q_dense/kernel/Regularizer/Const:output:0*
T0*
_output_shapes
: e
 q_dense/kernel/Regularizer/mul/xConst*
_output_shapes
: *
dtype0*
valueB
 *o:
q_dense/kernel/Regularizer/mulMul)q_dense/kernel/Regularizer/mul/x:output:0'q_dense/kernel/Regularizer/Sum:output:0*
T0*
_output_shapes
: Y
IdentityIdentity
add_11:z:0^NoOp*
T0*'
_output_shapes
:????????? ζ
NoOpNoOp^ReadVariableOp^ReadVariableOp_1^ReadVariableOp_2^ReadVariableOp_3^ReadVariableOp_4^ReadVariableOp_5.^q_dense/kernel/Regularizer/Abs/ReadVariableOp*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime**
_input_shapes
:?????????9: : 2 
ReadVariableOpReadVariableOp2$
ReadVariableOp_1ReadVariableOp_12$
ReadVariableOp_2ReadVariableOp_22$
ReadVariableOp_3ReadVariableOp_32$
ReadVariableOp_4ReadVariableOp_42$
ReadVariableOp_5ReadVariableOp_52^
-q_dense/kernel/Regularizer/Abs/ReadVariableOp-q_dense/kernel/Regularizer/Abs/ReadVariableOp:O K
'
_output_shapes
:?????????9
 
_user_specified_nameinputs
Ώ#
Ρ
?__inference_model_layer_call_and_return_conditional_losses_1281

inputs
q_dense_1253:9 
q_dense_1255:  
q_dense_1_1258: 
q_dense_1_1260:
mu_1263:
mu_1265:
identity’mu/StatefulPartitionedCall’q_dense/StatefulPartitionedCall’-q_dense/kernel/Regularizer/Abs/ReadVariableOp’!q_dense_1/StatefulPartitionedCall’/q_dense_1/kernel/Regularizer/Abs/ReadVariableOp½
q_activation/PartitionedCallPartitionedCallinputs*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????9* 
_read_only_resource_inputs
 *-
config_proto

CPU

GPU 2J 8 *N
fIRG
E__inference_q_activation_layer_call_and_return_conditional_losses_813
q_dense/StatefulPartitionedCallStatefulPartitionedCall%q_activation/PartitionedCall:output:0q_dense_1253q_dense_1255*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:????????? *$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8 *I
fDRB
@__inference_q_dense_layer_call_and_return_conditional_losses_934
!q_dense_1/StatefulPartitionedCallStatefulPartitionedCall(q_dense/StatefulPartitionedCall:output:0q_dense_1_1258q_dense_1_1260*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8 *L
fGRE
C__inference_q_dense_1_layer_call_and_return_conditional_losses_1059φ
mu/StatefulPartitionedCallStatefulPartitionedCall*q_dense_1/StatefulPartitionedCall:output:0mu_1263mu_1265*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8 *E
f@R>
<__inference_mu_layer_call_and_return_conditional_losses_1160z
-q_dense/kernel/Regularizer/Abs/ReadVariableOpReadVariableOpq_dense_1253*
_output_shapes

:9 *
dtype0
q_dense/kernel/Regularizer/AbsAbs5q_dense/kernel/Regularizer/Abs/ReadVariableOp:value:0*
T0*
_output_shapes

:9 q
 q_dense/kernel/Regularizer/ConstConst*
_output_shapes
:*
dtype0*
valueB"       
q_dense/kernel/Regularizer/SumSum"q_dense/kernel/Regularizer/Abs:y:0)q_dense/kernel/Regularizer/Const:output:0*
T0*
_output_shapes
: e
 q_dense/kernel/Regularizer/mul/xConst*
_output_shapes
: *
dtype0*
valueB
 *o:
q_dense/kernel/Regularizer/mulMul)q_dense/kernel/Regularizer/mul/x:output:0'q_dense/kernel/Regularizer/Sum:output:0*
T0*
_output_shapes
: ~
/q_dense_1/kernel/Regularizer/Abs/ReadVariableOpReadVariableOpq_dense_1_1258*
_output_shapes

: *
dtype0
 q_dense_1/kernel/Regularizer/AbsAbs7q_dense_1/kernel/Regularizer/Abs/ReadVariableOp:value:0*
T0*
_output_shapes

: s
"q_dense_1/kernel/Regularizer/ConstConst*
_output_shapes
:*
dtype0*
valueB"       
 q_dense_1/kernel/Regularizer/SumSum$q_dense_1/kernel/Regularizer/Abs:y:0+q_dense_1/kernel/Regularizer/Const:output:0*
T0*
_output_shapes
: g
"q_dense_1/kernel/Regularizer/mul/xConst*
_output_shapes
: *
dtype0*
valueB
 *     
 q_dense_1/kernel/Regularizer/mulMul+q_dense_1/kernel/Regularizer/mul/x:output:0)q_dense_1/kernel/Regularizer/Sum:output:0*
T0*
_output_shapes
: r
IdentityIdentity#mu/StatefulPartitionedCall:output:0^NoOp*
T0*'
_output_shapes
:?????????
NoOpNoOp^mu/StatefulPartitionedCall ^q_dense/StatefulPartitionedCall.^q_dense/kernel/Regularizer/Abs/ReadVariableOp"^q_dense_1/StatefulPartitionedCall0^q_dense_1/kernel/Regularizer/Abs/ReadVariableOp*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*2
_input_shapes!
:?????????9: : : : : : 28
mu/StatefulPartitionedCallmu/StatefulPartitionedCall2B
q_dense/StatefulPartitionedCallq_dense/StatefulPartitionedCall2^
-q_dense/kernel/Regularizer/Abs/ReadVariableOp-q_dense/kernel/Regularizer/Abs/ReadVariableOp2F
!q_dense_1/StatefulPartitionedCall!q_dense_1/StatefulPartitionedCall2b
/q_dense_1/kernel/Regularizer/Abs/ReadVariableOp/q_dense_1/kernel/Regularizer/Abs/ReadVariableOp:O K
'
_output_shapes
:?????????9
 
_user_specified_nameinputs
Μ
ζ
 __inference__traced_restore_2645
file_prefix1
assignvariableop_q_dense_kernel:9 -
assignvariableop_1_q_dense_bias: 5
#assignvariableop_2_q_dense_1_kernel: /
!assignvariableop_3_q_dense_1_bias:.
assignvariableop_4_mu_kernel:(
assignvariableop_5_mu_bias:

identity_7’AssignVariableOp’AssignVariableOp_1’AssignVariableOp_2’AssignVariableOp_3’AssignVariableOp_4’AssignVariableOp_5Χ
RestoreV2/tensor_namesConst"/device:CPU:0*
_output_shapes
:*
dtype0*ύ
valueσBπB6layer_with_weights-0/kernel/.ATTRIBUTES/VARIABLE_VALUEB4layer_with_weights-0/bias/.ATTRIBUTES/VARIABLE_VALUEB6layer_with_weights-1/kernel/.ATTRIBUTES/VARIABLE_VALUEB4layer_with_weights-1/bias/.ATTRIBUTES/VARIABLE_VALUEB6layer_with_weights-2/kernel/.ATTRIBUTES/VARIABLE_VALUEB4layer_with_weights-2/bias/.ATTRIBUTES/VARIABLE_VALUEB_CHECKPOINTABLE_OBJECT_GRAPH~
RestoreV2/shape_and_slicesConst"/device:CPU:0*
_output_shapes
:*
dtype0*!
valueBB B B B B B B Α
	RestoreV2	RestoreV2file_prefixRestoreV2/tensor_names:output:0#RestoreV2/shape_and_slices:output:0"/device:CPU:0*0
_output_shapes
:::::::*
dtypes
	2[
IdentityIdentityRestoreV2:tensors:0"/device:CPU:0*
T0*
_output_shapes
:
AssignVariableOpAssignVariableOpassignvariableop_q_dense_kernelIdentity:output:0"/device:CPU:0*
_output_shapes
 *
dtype0]

Identity_1IdentityRestoreV2:tensors:1"/device:CPU:0*
T0*
_output_shapes
:
AssignVariableOp_1AssignVariableOpassignvariableop_1_q_dense_biasIdentity_1:output:0"/device:CPU:0*
_output_shapes
 *
dtype0]

Identity_2IdentityRestoreV2:tensors:2"/device:CPU:0*
T0*
_output_shapes
:
AssignVariableOp_2AssignVariableOp#assignvariableop_2_q_dense_1_kernelIdentity_2:output:0"/device:CPU:0*
_output_shapes
 *
dtype0]

Identity_3IdentityRestoreV2:tensors:3"/device:CPU:0*
T0*
_output_shapes
:
AssignVariableOp_3AssignVariableOp!assignvariableop_3_q_dense_1_biasIdentity_3:output:0"/device:CPU:0*
_output_shapes
 *
dtype0]

Identity_4IdentityRestoreV2:tensors:4"/device:CPU:0*
T0*
_output_shapes
:
AssignVariableOp_4AssignVariableOpassignvariableop_4_mu_kernelIdentity_4:output:0"/device:CPU:0*
_output_shapes
 *
dtype0]

Identity_5IdentityRestoreV2:tensors:5"/device:CPU:0*
T0*
_output_shapes
:
AssignVariableOp_5AssignVariableOpassignvariableop_5_mu_biasIdentity_5:output:0"/device:CPU:0*
_output_shapes
 *
dtype01
NoOpNoOp"/device:CPU:0*
_output_shapes
 Φ

Identity_6Identityfile_prefix^AssignVariableOp^AssignVariableOp_1^AssignVariableOp_2^AssignVariableOp_3^AssignVariableOp_4^AssignVariableOp_5^NoOp"/device:CPU:0*
T0*
_output_shapes
: U

Identity_7IdentityIdentity_6:output:0^NoOp_1*
T0*
_output_shapes
: Δ
NoOp_1NoOp^AssignVariableOp^AssignVariableOp_1^AssignVariableOp_2^AssignVariableOp_3^AssignVariableOp_4^AssignVariableOp_5*"
_acd_function_control_output(*
_output_shapes
 "!

identity_7Identity_7:output:0*!
_input_shapes
: : : : : : : 2$
AssignVariableOpAssignVariableOp2(
AssignVariableOp_1AssignVariableOp_12(
AssignVariableOp_2AssignVariableOp_22(
AssignVariableOp_3AssignVariableOp_32(
AssignVariableOp_4AssignVariableOp_42(
AssignVariableOp_5AssignVariableOp_5:C ?

_output_shapes
: 
%
_user_specified_namefile_prefix
έX
Ψ
C__inference_q_dense_1_layer_call_and_return_conditional_losses_1059

inputs)
readvariableop_resource: '
readvariableop_3_resource:
identity’ReadVariableOp’ReadVariableOp_1’ReadVariableOp_2’ReadVariableOp_3’ReadVariableOp_4’ReadVariableOp_5’/q_dense_1/kernel/Regularizer/Abs/ReadVariableOpG
Pow/xConst*
_output_shapes
: *
dtype0*
value	B :G
Pow/yConst*
_output_shapes
: *
dtype0*
value	B :K
PowPowPow/x:output:0Pow/y:output:0*
T0*
_output_shapes
: E
CastCastPow:z:0*

DstT0*

SrcT0*
_output_shapes
: f
ReadVariableOpReadVariableOpreadvariableop_resource*
_output_shapes

: *
dtype0J
mul/yConst*
_output_shapes
: *
dtype0*
valueB
 *   B[
mulMulReadVariableOp:value:0mul/y:output:0*
T0*
_output_shapes

: N
truedivRealDivmul:z:0Cast:y:0*
T0*
_output_shapes

: @
NegNegtruediv:z:0*
T0*
_output_shapes

: D
RoundRoundtruediv:z:0*
T0*
_output_shapes

: I
addAddV2Neg:y:0	Round:y:0*
T0*
_output_shapes

: N
StopGradientStopGradientadd:z:0*
T0*
_output_shapes

: [
add_1AddV2truediv:z:0StopGradient:output:0*
T0*
_output_shapes

: \
clip_by_value/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 *  ψAv
clip_by_value/MinimumMinimum	add_1:z:0 clip_by_value/Minimum/y:output:0*
T0*
_output_shapes

: T
clip_by_value/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Βv
clip_by_valueMaximumclip_by_value/Minimum:z:0clip_by_value/y:output:0*
T0*
_output_shapes

: R
mul_1MulCast:y:0clip_by_value:z:0*
T0*
_output_shapes

: P
truediv_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   B^
	truediv_1RealDiv	mul_1:z:0truediv_1/y:output:0*
T0*
_output_shapes

: L
mul_2/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?V
mul_2Mulmul_2/x:output:0truediv_1:z:0*
T0*
_output_shapes

: h
ReadVariableOp_1ReadVariableOpreadvariableop_resource*
_output_shapes

: *
dtype0O
Neg_1NegReadVariableOp_1:value:0*
T0*
_output_shapes

: M
add_2AddV2	Neg_1:y:0	mul_2:z:0*
T0*
_output_shapes

: L
mul_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?R
mul_3Mulmul_3/x:output:0	add_2:z:0*
T0*
_output_shapes

: R
StopGradient_1StopGradient	mul_3:z:0*
T0*
_output_shapes

: h
ReadVariableOp_2ReadVariableOpreadvariableop_resource*
_output_shapes

: *
dtype0j
add_3AddV2ReadVariableOp_2:value:0StopGradient_1:output:0*
T0*
_output_shapes

: U
MatMulMatMulinputs	add_3:z:0*
T0*'
_output_shapes
:?????????I
Pow_1/xConst*
_output_shapes
: *
dtype0*
value	B :I
Pow_1/yConst*
_output_shapes
: *
dtype0*
value	B :Q
Pow_1PowPow_1/x:output:0Pow_1/y:output:0*
T0*
_output_shapes
: I
Cast_1Cast	Pow_1:z:0*

DstT0*

SrcT0*
_output_shapes
: f
ReadVariableOp_3ReadVariableOpreadvariableop_3_resource*
_output_shapes
:*
dtype0L
mul_4/yConst*
_output_shapes
: *
dtype0*
valueB
 *  E]
mul_4MulReadVariableOp_3:value:0mul_4/y:output:0*
T0*
_output_shapes
:P
	truediv_2RealDiv	mul_4:z:0
Cast_1:y:0*
T0*
_output_shapes
:@
Neg_2Negtruediv_2:z:0*
T0*
_output_shapes
:D
Round_1Roundtruediv_2:z:0*
T0*
_output_shapes
:K
add_4AddV2	Neg_2:y:0Round_1:y:0*
T0*
_output_shapes
:N
StopGradient_2StopGradient	add_4:z:0*
T0*
_output_shapes
:[
add_5AddV2truediv_2:z:0StopGradient_2:output:0*
T0*
_output_shapes
:^
clip_by_value_1/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * πEv
clip_by_value_1/MinimumMinimum	add_5:z:0"clip_by_value_1/Minimum/y:output:0*
T0*
_output_shapes
:V
clip_by_value_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *  Εx
clip_by_value_1Maximumclip_by_value_1/Minimum:z:0clip_by_value_1/y:output:0*
T0*
_output_shapes
:R
mul_5Mul
Cast_1:y:0clip_by_value_1:z:0*
T0*
_output_shapes
:P
truediv_3/yConst*
_output_shapes
: *
dtype0*
valueB
 *  EZ
	truediv_3RealDiv	mul_5:z:0truediv_3/y:output:0*
T0*
_output_shapes
:L
mul_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?R
mul_6Mulmul_6/x:output:0truediv_3:z:0*
T0*
_output_shapes
:f
ReadVariableOp_4ReadVariableOpreadvariableop_3_resource*
_output_shapes
:*
dtype0K
Neg_3NegReadVariableOp_4:value:0*
T0*
_output_shapes
:I
add_6AddV2	Neg_3:y:0	mul_6:z:0*
T0*
_output_shapes
:L
mul_7/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?N
mul_7Mulmul_7/x:output:0	add_6:z:0*
T0*
_output_shapes
:N
StopGradient_3StopGradient	mul_7:z:0*
T0*
_output_shapes
:f
ReadVariableOp_5ReadVariableOpreadvariableop_3_resource*
_output_shapes
:*
dtype0f
add_7AddV2ReadVariableOp_5:value:0StopGradient_3:output:0*
T0*
_output_shapes
:a
BiasAddBiasAddMatMul:product:0	add_7:z:0*
T0*'
_output_shapes
:?????????I
Pow_2/xConst*
_output_shapes
: *
dtype0*
value	B :I
Pow_2/yConst*
_output_shapes
: *
dtype0*
value	B :Q
Pow_2PowPow_2/x:output:0Pow_2/y:output:0*
T0*
_output_shapes
: I
Cast_2Cast	Pow_2:z:0*

DstT0*

SrcT0*
_output_shapes
: I
Pow_3/xConst*
_output_shapes
: *
dtype0*
value	B :I
Pow_3/yConst*
_output_shapes
: *
dtype0*
value	B :Q
Pow_3PowPow_3/x:output:0Pow_3/y:output:0*
T0*
_output_shapes
: I
Cast_3Cast	Pow_3:z:0*

DstT0*

SrcT0*
_output_shapes
: J
ConstConst*
_output_shapes
: *
dtype0*
valueB
 *   @J
Cast_4/xConst*
_output_shapes
: *
dtype0*
value	B :Q
Cast_4CastCast_4/x:output:0*

DstT0*

SrcT0*
_output_shapes
: J
sub/yConst*
_output_shapes
: *
dtype0*
valueB
 *  PAG
subSub
Cast_4:y:0sub/y:output:0*
T0*
_output_shapes
: F
Pow_4PowConst:output:0sub:z:0*
T0*
_output_shapes
: D
sub_1Sub
Cast_3:y:0	Pow_4:z:0*
T0*
_output_shapes
: e
	LessEqual	LessEqualBiasAdd:output:0	sub_1:z:0*
T0*'
_output_shapes
:?????????P
ReluReluBiasAdd:output:0*
T0*'
_output_shapes
:?????????O
ones_like/ShapeShapeBiasAdd:output:0*
T0*
_output_shapes
:T
ones_like/ConstConst*
_output_shapes
: *
dtype0*
valueB
 *  ?w
	ones_likeFillones_like/Shape:output:0ones_like/Const:output:0*
T0*'
_output_shapes
:?????????D
sub_2Sub
Cast_3:y:0	Pow_4:z:0*
T0*
_output_shapes
: ]
mul_8Mulones_like:output:0	sub_2:z:0*
T0*'
_output_shapes
:?????????t
SelectV2SelectV2LessEqual:z:0Relu:activations:0	mul_8:z:0*
T0*'
_output_shapes
:?????????\
mul_9MulBiasAdd:output:0
Cast_2:y:0*
T0*'
_output_shapes
:?????????]
	truediv_4RealDiv	mul_9:z:0
Cast_3:y:0*
T0*'
_output_shapes
:?????????M
Neg_4Negtruediv_4:z:0*
T0*'
_output_shapes
:?????????Q
Round_2Roundtruediv_4:z:0*
T0*'
_output_shapes
:?????????X
add_8AddV2	Neg_4:y:0Round_2:y:0*
T0*'
_output_shapes
:?????????[
StopGradient_4StopGradient	add_8:z:0*
T0*'
_output_shapes
:?????????h
add_9AddV2truediv_4:z:0StopGradient_4:output:0*
T0*'
_output_shapes
:?????????]
	truediv_5RealDiv	add_9:z:0
Cast_2:y:0*
T0*'
_output_shapes
:?????????P
truediv_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?W
	truediv_6RealDivtruediv_6/x:output:0
Cast_2:y:0*
T0*
_output_shapes
: L
sub_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?N
sub_3Subsub_3/x:output:0truediv_6:z:0*
T0*
_output_shapes
: n
clip_by_value_2/MinimumMinimumtruediv_5:z:0	sub_3:z:0*
T0*'
_output_shapes
:?????????V
clip_by_value_2/yConst*
_output_shapes
: *
dtype0*
valueB
 *    
clip_by_value_2Maximumclip_by_value_2/Minimum:z:0clip_by_value_2/y:output:0*
T0*'
_output_shapes
:?????????`
mul_10Mul
Cast_3:y:0clip_by_value_2:z:0*
T0*'
_output_shapes
:?????????Q
Neg_5NegSelectV2:output:0*
T0*'
_output_shapes
:?????????X
add_10AddV2	Neg_5:y:0
mul_10:z:0*
T0*'
_output_shapes
:?????????M
mul_11/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?^
mul_11Mulmul_11/x:output:0
add_10:z:0*
T0*'
_output_shapes
:?????????\
StopGradient_5StopGradient
mul_11:z:0*
T0*'
_output_shapes
:?????????m
add_11AddV2SelectV2:output:0StopGradient_5:output:0*
T0*'
_output_shapes
:?????????
/q_dense_1/kernel/Regularizer/Abs/ReadVariableOpReadVariableOpreadvariableop_resource*
_output_shapes

: *
dtype0
 q_dense_1/kernel/Regularizer/AbsAbs7q_dense_1/kernel/Regularizer/Abs/ReadVariableOp:value:0*
T0*
_output_shapes

: s
"q_dense_1/kernel/Regularizer/ConstConst*
_output_shapes
:*
dtype0*
valueB"       
 q_dense_1/kernel/Regularizer/SumSum$q_dense_1/kernel/Regularizer/Abs:y:0+q_dense_1/kernel/Regularizer/Const:output:0*
T0*
_output_shapes
: g
"q_dense_1/kernel/Regularizer/mul/xConst*
_output_shapes
: *
dtype0*
valueB
 *     
 q_dense_1/kernel/Regularizer/mulMul+q_dense_1/kernel/Regularizer/mul/x:output:0)q_dense_1/kernel/Regularizer/Sum:output:0*
T0*
_output_shapes
: Y
IdentityIdentity
add_11:z:0^NoOp*
T0*'
_output_shapes
:?????????θ
NoOpNoOp^ReadVariableOp^ReadVariableOp_1^ReadVariableOp_2^ReadVariableOp_3^ReadVariableOp_4^ReadVariableOp_50^q_dense_1/kernel/Regularizer/Abs/ReadVariableOp*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime**
_input_shapes
:????????? : : 2 
ReadVariableOpReadVariableOp2$
ReadVariableOp_1ReadVariableOp_12$
ReadVariableOp_2ReadVariableOp_22$
ReadVariableOp_3ReadVariableOp_32$
ReadVariableOp_4ReadVariableOp_42$
ReadVariableOp_5ReadVariableOp_52b
/q_dense_1/kernel/Regularizer/Abs/ReadVariableOp/q_dense_1/kernel/Regularizer/Abs/ReadVariableOp:O K
'
_output_shapes
:????????? 
 
_user_specified_nameinputs
ΐ

(__inference_q_dense_1_layer_call_fn_2331

inputs
unknown: 
	unknown_0:
identity’StatefulPartitionedCallΨ
StatefulPartitionedCallStatefulPartitionedCallinputsunknown	unknown_0*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8 *L
fGRE
C__inference_q_dense_1_layer_call_and_return_conditional_losses_1059o
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*'
_output_shapes
:?????????`
NoOpNoOp^StatefulPartitionedCall*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime**
_input_shapes
:????????? : : 22
StatefulPartitionedCallStatefulPartitionedCall:O K
'
_output_shapes
:????????? 
 
_user_specified_nameinputs
Ξ
a
E__inference_q_activation_layer_call_and_return_conditional_losses_813

inputs
identityG
Pow/xConst*
_output_shapes
: *
dtype0*
value	B :G
Pow/yConst*
_output_shapes
: *
dtype0*
value	B :K
PowPowPow/x:output:0Pow/y:output:0*
T0*
_output_shapes
: E
CastCastPow:z:0*

DstT0*

SrcT0*
_output_shapes
: J
mul/yConst*
_output_shapes
: *
dtype0*
valueB
 *   DT
mulMulinputsmul/y:output:0*
T0*'
_output_shapes
:?????????9W
truedivRealDivmul:z:0Cast:y:0*
T0*'
_output_shapes
:?????????9I
NegNegtruediv:z:0*
T0*'
_output_shapes
:?????????9M
RoundRoundtruediv:z:0*
T0*'
_output_shapes
:?????????9R
addAddV2Neg:y:0	Round:y:0*
T0*'
_output_shapes
:?????????9W
StopGradientStopGradientadd:z:0*
T0*'
_output_shapes
:?????????9d
add_1AddV2truediv:z:0StopGradient:output:0*
T0*'
_output_shapes
:?????????9\
clip_by_value/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * ?C
clip_by_value/MinimumMinimum	add_1:z:0 clip_by_value/Minimum/y:output:0*
T0*'
_output_shapes
:?????????9T
clip_by_value/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Δ
clip_by_valueMaximumclip_by_value/Minimum:z:0clip_by_value/y:output:0*
T0*'
_output_shapes
:?????????9[
mul_1MulCast:y:0clip_by_value:z:0*
T0*'
_output_shapes
:?????????9P
truediv_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Dg
	truediv_1RealDiv	mul_1:z:0truediv_1/y:output:0*
T0*'
_output_shapes
:?????????9L
mul_2/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?_
mul_2Mulmul_2/x:output:0truediv_1:z:0*
T0*'
_output_shapes
:?????????9F
Neg_1Neginputs*
T0*'
_output_shapes
:?????????9V
add_2AddV2	Neg_1:y:0	mul_2:z:0*
T0*'
_output_shapes
:?????????9L
mul_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?[
mul_3Mulmul_3/x:output:0	add_2:z:0*
T0*'
_output_shapes
:?????????9[
StopGradient_1StopGradient	mul_3:z:0*
T0*'
_output_shapes
:?????????9a
add_3AddV2inputsStopGradient_1:output:0*
T0*'
_output_shapes
:?????????9Q
IdentityIdentity	add_3:z:0*
T0*'
_output_shapes
:?????????9"
identityIdentity:output:0*(
_construction_contextkEagerRuntime*&
_input_shapes
:?????????9:O K
'
_output_shapes
:?????????9
 
_user_specified_nameinputs
γ
ώ
$__inference_model_layer_call_fn_1313
input_1
unknown:9 
	unknown_0: 
	unknown_1: 
	unknown_2:
	unknown_3:
	unknown_4:
identity’StatefulPartitionedCall
StatefulPartitionedCallStatefulPartitionedCallinput_1unknown	unknown_0	unknown_1	unknown_2	unknown_3	unknown_4*
Tin
	2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*(
_read_only_resource_inputs

*-
config_proto

CPU

GPU 2J 8 *H
fCRA
?__inference_model_layer_call_and_return_conditional_losses_1281o
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*'
_output_shapes
:?????????`
NoOpNoOp^StatefulPartitionedCall*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*2
_input_shapes!
:?????????9: : : : : : 22
StatefulPartitionedCallStatefulPartitionedCall:P L
'
_output_shapes
:?????????9
!
_user_specified_name	input_1
²

!__inference_mu_layer_call_fn_2459

inputs
unknown:
	unknown_0:
identity’StatefulPartitionedCallΡ
StatefulPartitionedCallStatefulPartitionedCallinputsunknown	unknown_0*
Tin
2*
Tout
2*
_collective_manager_ids
 *'
_output_shapes
:?????????*$
_read_only_resource_inputs
*-
config_proto

CPU

GPU 2J 8 *E
f@R>
<__inference_mu_layer_call_and_return_conditional_losses_1160o
IdentityIdentity StatefulPartitionedCall:output:0^NoOp*
T0*'
_output_shapes
:?????????`
NoOpNoOp^StatefulPartitionedCall*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime**
_input_shapes
:?????????: : 22
StatefulPartitionedCallStatefulPartitionedCall:O K
'
_output_shapes
:?????????
 
_user_specified_nameinputs
―E

<__inference_mu_layer_call_and_return_conditional_losses_1160

inputs)
readvariableop_resource:'
readvariableop_3_resource:
identity’ReadVariableOp’ReadVariableOp_1’ReadVariableOp_2’ReadVariableOp_3’ReadVariableOp_4’ReadVariableOp_5G
Pow/xConst*
_output_shapes
: *
dtype0*
value	B :G
Pow/yConst*
_output_shapes
: *
dtype0*
value	B :K
PowPowPow/x:output:0Pow/y:output:0*
T0*
_output_shapes
: E
CastCastPow:z:0*

DstT0*

SrcT0*
_output_shapes
: f
ReadVariableOpReadVariableOpreadvariableop_resource*
_output_shapes

:*
dtype0J
mul/yConst*
_output_shapes
: *
dtype0*
valueB
 *   B[
mulMulReadVariableOp:value:0mul/y:output:0*
T0*
_output_shapes

:N
truedivRealDivmul:z:0Cast:y:0*
T0*
_output_shapes

:@
NegNegtruediv:z:0*
T0*
_output_shapes

:D
RoundRoundtruediv:z:0*
T0*
_output_shapes

:I
addAddV2Neg:y:0	Round:y:0*
T0*
_output_shapes

:N
StopGradientStopGradientadd:z:0*
T0*
_output_shapes

:[
add_1AddV2truediv:z:0StopGradient:output:0*
T0*
_output_shapes

:\
clip_by_value/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 *  ψAv
clip_by_value/MinimumMinimum	add_1:z:0 clip_by_value/Minimum/y:output:0*
T0*
_output_shapes

:T
clip_by_value/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Βv
clip_by_valueMaximumclip_by_value/Minimum:z:0clip_by_value/y:output:0*
T0*
_output_shapes

:R
mul_1MulCast:y:0clip_by_value:z:0*
T0*
_output_shapes

:P
truediv_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   B^
	truediv_1RealDiv	mul_1:z:0truediv_1/y:output:0*
T0*
_output_shapes

:L
mul_2/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?V
mul_2Mulmul_2/x:output:0truediv_1:z:0*
T0*
_output_shapes

:h
ReadVariableOp_1ReadVariableOpreadvariableop_resource*
_output_shapes

:*
dtype0O
Neg_1NegReadVariableOp_1:value:0*
T0*
_output_shapes

:M
add_2AddV2	Neg_1:y:0	mul_2:z:0*
T0*
_output_shapes

:L
mul_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?R
mul_3Mulmul_3/x:output:0	add_2:z:0*
T0*
_output_shapes

:R
StopGradient_1StopGradient	mul_3:z:0*
T0*
_output_shapes

:h
ReadVariableOp_2ReadVariableOpreadvariableop_resource*
_output_shapes

:*
dtype0j
add_3AddV2ReadVariableOp_2:value:0StopGradient_1:output:0*
T0*
_output_shapes

:U
MatMulMatMulinputs	add_3:z:0*
T0*'
_output_shapes
:?????????I
Pow_1/xConst*
_output_shapes
: *
dtype0*
value	B :I
Pow_1/yConst*
_output_shapes
: *
dtype0*
value	B :Q
Pow_1PowPow_1/x:output:0Pow_1/y:output:0*
T0*
_output_shapes
: I
Cast_1Cast	Pow_1:z:0*

DstT0*

SrcT0*
_output_shapes
: f
ReadVariableOp_3ReadVariableOpreadvariableop_3_resource*
_output_shapes
:*
dtype0L
mul_4/yConst*
_output_shapes
: *
dtype0*
valueB
 *   D]
mul_4MulReadVariableOp_3:value:0mul_4/y:output:0*
T0*
_output_shapes
:P
	truediv_2RealDiv	mul_4:z:0
Cast_1:y:0*
T0*
_output_shapes
:@
Neg_2Negtruediv_2:z:0*
T0*
_output_shapes
:D
Round_1Roundtruediv_2:z:0*
T0*
_output_shapes
:K
add_4AddV2	Neg_2:y:0Round_1:y:0*
T0*
_output_shapes
:N
StopGradient_2StopGradient	add_4:z:0*
T0*
_output_shapes
:[
add_5AddV2truediv_2:z:0StopGradient_2:output:0*
T0*
_output_shapes
:^
clip_by_value_1/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * ?Cv
clip_by_value_1/MinimumMinimum	add_5:z:0"clip_by_value_1/Minimum/y:output:0*
T0*
_output_shapes
:V
clip_by_value_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Δx
clip_by_value_1Maximumclip_by_value_1/Minimum:z:0clip_by_value_1/y:output:0*
T0*
_output_shapes
:R
mul_5Mul
Cast_1:y:0clip_by_value_1:z:0*
T0*
_output_shapes
:P
truediv_3/yConst*
_output_shapes
: *
dtype0*
valueB
 *   DZ
	truediv_3RealDiv	mul_5:z:0truediv_3/y:output:0*
T0*
_output_shapes
:L
mul_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?R
mul_6Mulmul_6/x:output:0truediv_3:z:0*
T0*
_output_shapes
:f
ReadVariableOp_4ReadVariableOpreadvariableop_3_resource*
_output_shapes
:*
dtype0K
Neg_3NegReadVariableOp_4:value:0*
T0*
_output_shapes
:I
add_6AddV2	Neg_3:y:0	mul_6:z:0*
T0*
_output_shapes
:L
mul_7/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?N
mul_7Mulmul_7/x:output:0	add_6:z:0*
T0*
_output_shapes
:N
StopGradient_3StopGradient	mul_7:z:0*
T0*
_output_shapes
:f
ReadVariableOp_5ReadVariableOpreadvariableop_3_resource*
_output_shapes
:*
dtype0f
add_7AddV2ReadVariableOp_5:value:0StopGradient_3:output:0*
T0*
_output_shapes
:a
BiasAddBiasAddMatMul:product:0	add_7:z:0*
T0*'
_output_shapes
:?????????I
Pow_2/xConst*
_output_shapes
: *
dtype0*
value	B :I
Pow_2/yConst*
_output_shapes
: *
dtype0*
value	B :Q
Pow_2PowPow_2/x:output:0Pow_2/y:output:0*
T0*
_output_shapes
: I
Cast_2Cast	Pow_2:z:0*

DstT0*

SrcT0*
_output_shapes
: L
mul_8/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Db
mul_8MulBiasAdd:output:0mul_8/y:output:0*
T0*'
_output_shapes
:?????????]
	truediv_4RealDiv	mul_8:z:0
Cast_2:y:0*
T0*'
_output_shapes
:?????????M
Neg_4Negtruediv_4:z:0*
T0*'
_output_shapes
:?????????Q
Round_2Roundtruediv_4:z:0*
T0*'
_output_shapes
:?????????X
add_8AddV2	Neg_4:y:0Round_2:y:0*
T0*'
_output_shapes
:?????????[
StopGradient_4StopGradient	add_8:z:0*
T0*'
_output_shapes
:?????????h
add_9AddV2truediv_4:z:0StopGradient_4:output:0*
T0*'
_output_shapes
:?????????^
clip_by_value_2/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * ?C
clip_by_value_2/MinimumMinimum	add_9:z:0"clip_by_value_2/Minimum/y:output:0*
T0*'
_output_shapes
:?????????V
clip_by_value_2/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Δ
clip_by_value_2Maximumclip_by_value_2/Minimum:z:0clip_by_value_2/y:output:0*
T0*'
_output_shapes
:?????????_
mul_9Mul
Cast_2:y:0clip_by_value_2:z:0*
T0*'
_output_shapes
:?????????P
truediv_5/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Dg
	truediv_5RealDiv	mul_9:z:0truediv_5/y:output:0*
T0*'
_output_shapes
:?????????M
mul_10/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?a
mul_10Mulmul_10/x:output:0truediv_5:z:0*
T0*'
_output_shapes
:?????????P
Neg_5NegBiasAdd:output:0*
T0*'
_output_shapes
:?????????X
add_10AddV2	Neg_5:y:0
mul_10:z:0*
T0*'
_output_shapes
:?????????M
mul_11/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?^
mul_11Mulmul_11/x:output:0
add_10:z:0*
T0*'
_output_shapes
:?????????\
StopGradient_5StopGradient
mul_11:z:0*
T0*'
_output_shapes
:?????????l
add_11AddV2BiasAdd:output:0StopGradient_5:output:0*
T0*'
_output_shapes
:?????????Y
IdentityIdentity
add_11:z:0^NoOp*
T0*'
_output_shapes
:?????????Ά
NoOpNoOp^ReadVariableOp^ReadVariableOp_1^ReadVariableOp_2^ReadVariableOp_3^ReadVariableOp_4^ReadVariableOp_5*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime**
_input_shapes
:?????????: : 2 
ReadVariableOpReadVariableOp2$
ReadVariableOp_1ReadVariableOp_12$
ReadVariableOp_2ReadVariableOp_22$
ReadVariableOp_3ReadVariableOp_32$
ReadVariableOp_4ReadVariableOp_42$
ReadVariableOp_5ReadVariableOp_5:O K
'
_output_shapes
:?????????
 
_user_specified_nameinputs
¦
«
__inference_loss_fn_1_2576J
8q_dense_1_kernel_regularizer_abs_readvariableop_resource: 
identity’/q_dense_1/kernel/Regularizer/Abs/ReadVariableOp¨
/q_dense_1/kernel/Regularizer/Abs/ReadVariableOpReadVariableOp8q_dense_1_kernel_regularizer_abs_readvariableop_resource*
_output_shapes

: *
dtype0
 q_dense_1/kernel/Regularizer/AbsAbs7q_dense_1/kernel/Regularizer/Abs/ReadVariableOp:value:0*
T0*
_output_shapes

: s
"q_dense_1/kernel/Regularizer/ConstConst*
_output_shapes
:*
dtype0*
valueB"       
 q_dense_1/kernel/Regularizer/SumSum$q_dense_1/kernel/Regularizer/Abs:y:0+q_dense_1/kernel/Regularizer/Const:output:0*
T0*
_output_shapes
: g
"q_dense_1/kernel/Regularizer/mul/xConst*
_output_shapes
: *
dtype0*
valueB
 *     
 q_dense_1/kernel/Regularizer/mulMul+q_dense_1/kernel/Regularizer/mul/x:output:0)q_dense_1/kernel/Regularizer/Sum:output:0*
T0*
_output_shapes
: b
IdentityIdentity$q_dense_1/kernel/Regularizer/mul:z:0^NoOp*
T0*
_output_shapes
: x
NoOpNoOp0^q_dense_1/kernel/Regularizer/Abs/ReadVariableOp*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*
_input_shapes
: 2b
/q_dense_1/kernel/Regularizer/Abs/ReadVariableOp/q_dense_1/kernel/Regularizer/Abs/ReadVariableOp
Υ²
΄
?__inference_model_layer_call_and_return_conditional_losses_1806

inputs1
q_dense_readvariableop_resource:9 /
!q_dense_readvariableop_3_resource: 3
!q_dense_1_readvariableop_resource: 1
#q_dense_1_readvariableop_3_resource:,
mu_readvariableop_resource:*
mu_readvariableop_3_resource:
identity’mu/ReadVariableOp’mu/ReadVariableOp_1’mu/ReadVariableOp_2’mu/ReadVariableOp_3’mu/ReadVariableOp_4’mu/ReadVariableOp_5’q_dense/ReadVariableOp’q_dense/ReadVariableOp_1’q_dense/ReadVariableOp_2’q_dense/ReadVariableOp_3’q_dense/ReadVariableOp_4’q_dense/ReadVariableOp_5’-q_dense/kernel/Regularizer/Abs/ReadVariableOp’q_dense_1/ReadVariableOp’q_dense_1/ReadVariableOp_1’q_dense_1/ReadVariableOp_2’q_dense_1/ReadVariableOp_3’q_dense_1/ReadVariableOp_4’q_dense_1/ReadVariableOp_5’/q_dense_1/kernel/Regularizer/Abs/ReadVariableOpT
q_activation/Pow/xConst*
_output_shapes
: *
dtype0*
value	B :T
q_activation/Pow/yConst*
_output_shapes
: *
dtype0*
value	B :r
q_activation/PowPowq_activation/Pow/x:output:0q_activation/Pow/y:output:0*
T0*
_output_shapes
: _
q_activation/CastCastq_activation/Pow:z:0*

DstT0*

SrcT0*
_output_shapes
: W
q_activation/mul/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Dn
q_activation/mulMulinputsq_activation/mul/y:output:0*
T0*'
_output_shapes
:?????????9~
q_activation/truedivRealDivq_activation/mul:z:0q_activation/Cast:y:0*
T0*'
_output_shapes
:?????????9c
q_activation/NegNegq_activation/truediv:z:0*
T0*'
_output_shapes
:?????????9g
q_activation/RoundRoundq_activation/truediv:z:0*
T0*'
_output_shapes
:?????????9y
q_activation/addAddV2q_activation/Neg:y:0q_activation/Round:y:0*
T0*'
_output_shapes
:?????????9q
q_activation/StopGradientStopGradientq_activation/add:z:0*
T0*'
_output_shapes
:?????????9
q_activation/add_1AddV2q_activation/truediv:z:0"q_activation/StopGradient:output:0*
T0*'
_output_shapes
:?????????9i
$q_activation/clip_by_value/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * ?C¦
"q_activation/clip_by_value/MinimumMinimumq_activation/add_1:z:0-q_activation/clip_by_value/Minimum/y:output:0*
T0*'
_output_shapes
:?????????9a
q_activation/clip_by_value/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Δ¦
q_activation/clip_by_valueMaximum&q_activation/clip_by_value/Minimum:z:0%q_activation/clip_by_value/y:output:0*
T0*'
_output_shapes
:?????????9
q_activation/mul_1Mulq_activation/Cast:y:0q_activation/clip_by_value:z:0*
T0*'
_output_shapes
:?????????9]
q_activation/truediv_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   D
q_activation/truediv_1RealDivq_activation/mul_1:z:0!q_activation/truediv_1/y:output:0*
T0*'
_output_shapes
:?????????9Y
q_activation/mul_2/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?
q_activation/mul_2Mulq_activation/mul_2/x:output:0q_activation/truediv_1:z:0*
T0*'
_output_shapes
:?????????9S
q_activation/Neg_1Neginputs*
T0*'
_output_shapes
:?????????9}
q_activation/add_2AddV2q_activation/Neg_1:y:0q_activation/mul_2:z:0*
T0*'
_output_shapes
:?????????9Y
q_activation/mul_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?
q_activation/mul_3Mulq_activation/mul_3/x:output:0q_activation/add_2:z:0*
T0*'
_output_shapes
:?????????9u
q_activation/StopGradient_1StopGradientq_activation/mul_3:z:0*
T0*'
_output_shapes
:?????????9{
q_activation/add_3AddV2inputs$q_activation/StopGradient_1:output:0*
T0*'
_output_shapes
:?????????9O
q_dense/Pow/xConst*
_output_shapes
: *
dtype0*
value	B :O
q_dense/Pow/yConst*
_output_shapes
: *
dtype0*
value	B :c
q_dense/PowPowq_dense/Pow/x:output:0q_dense/Pow/y:output:0*
T0*
_output_shapes
: U
q_dense/CastCastq_dense/Pow:z:0*

DstT0*

SrcT0*
_output_shapes
: v
q_dense/ReadVariableOpReadVariableOpq_dense_readvariableop_resource*
_output_shapes

:9 *
dtype0R
q_dense/mul/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Bs
q_dense/mulMulq_dense/ReadVariableOp:value:0q_dense/mul/y:output:0*
T0*
_output_shapes

:9 f
q_dense/truedivRealDivq_dense/mul:z:0q_dense/Cast:y:0*
T0*
_output_shapes

:9 P
q_dense/NegNegq_dense/truediv:z:0*
T0*
_output_shapes

:9 T
q_dense/RoundRoundq_dense/truediv:z:0*
T0*
_output_shapes

:9 a
q_dense/addAddV2q_dense/Neg:y:0q_dense/Round:y:0*
T0*
_output_shapes

:9 ^
q_dense/StopGradientStopGradientq_dense/add:z:0*
T0*
_output_shapes

:9 s
q_dense/add_1AddV2q_dense/truediv:z:0q_dense/StopGradient:output:0*
T0*
_output_shapes

:9 d
q_dense/clip_by_value/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 *  ψA
q_dense/clip_by_value/MinimumMinimumq_dense/add_1:z:0(q_dense/clip_by_value/Minimum/y:output:0*
T0*
_output_shapes

:9 \
q_dense/clip_by_value/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Β
q_dense/clip_by_valueMaximum!q_dense/clip_by_value/Minimum:z:0 q_dense/clip_by_value/y:output:0*
T0*
_output_shapes

:9 j
q_dense/mul_1Mulq_dense/Cast:y:0q_dense/clip_by_value:z:0*
T0*
_output_shapes

:9 X
q_dense/truediv_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Bv
q_dense/truediv_1RealDivq_dense/mul_1:z:0q_dense/truediv_1/y:output:0*
T0*
_output_shapes

:9 T
q_dense/mul_2/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?n
q_dense/mul_2Mulq_dense/mul_2/x:output:0q_dense/truediv_1:z:0*
T0*
_output_shapes

:9 x
q_dense/ReadVariableOp_1ReadVariableOpq_dense_readvariableop_resource*
_output_shapes

:9 *
dtype0_
q_dense/Neg_1Neg q_dense/ReadVariableOp_1:value:0*
T0*
_output_shapes

:9 e
q_dense/add_2AddV2q_dense/Neg_1:y:0q_dense/mul_2:z:0*
T0*
_output_shapes

:9 T
q_dense/mul_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?j
q_dense/mul_3Mulq_dense/mul_3/x:output:0q_dense/add_2:z:0*
T0*
_output_shapes

:9 b
q_dense/StopGradient_1StopGradientq_dense/mul_3:z:0*
T0*
_output_shapes

:9 x
q_dense/ReadVariableOp_2ReadVariableOpq_dense_readvariableop_resource*
_output_shapes

:9 *
dtype0
q_dense/add_3AddV2 q_dense/ReadVariableOp_2:value:0q_dense/StopGradient_1:output:0*
T0*
_output_shapes

:9 u
q_dense/MatMulMatMulq_activation/add_3:z:0q_dense/add_3:z:0*
T0*'
_output_shapes
:????????? Q
q_dense/Pow_1/xConst*
_output_shapes
: *
dtype0*
value	B :Q
q_dense/Pow_1/yConst*
_output_shapes
: *
dtype0*
value	B :i
q_dense/Pow_1Powq_dense/Pow_1/x:output:0q_dense/Pow_1/y:output:0*
T0*
_output_shapes
: Y
q_dense/Cast_1Castq_dense/Pow_1:z:0*

DstT0*

SrcT0*
_output_shapes
: v
q_dense/ReadVariableOp_3ReadVariableOp!q_dense_readvariableop_3_resource*
_output_shapes
: *
dtype0T
q_dense/mul_4/yConst*
_output_shapes
: *
dtype0*
valueB
 *  Eu
q_dense/mul_4Mul q_dense/ReadVariableOp_3:value:0q_dense/mul_4/y:output:0*
T0*
_output_shapes
: h
q_dense/truediv_2RealDivq_dense/mul_4:z:0q_dense/Cast_1:y:0*
T0*
_output_shapes
: P
q_dense/Neg_2Negq_dense/truediv_2:z:0*
T0*
_output_shapes
: T
q_dense/Round_1Roundq_dense/truediv_2:z:0*
T0*
_output_shapes
: c
q_dense/add_4AddV2q_dense/Neg_2:y:0q_dense/Round_1:y:0*
T0*
_output_shapes
: ^
q_dense/StopGradient_2StopGradientq_dense/add_4:z:0*
T0*
_output_shapes
: s
q_dense/add_5AddV2q_dense/truediv_2:z:0q_dense/StopGradient_2:output:0*
T0*
_output_shapes
: f
!q_dense/clip_by_value_1/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * πE
q_dense/clip_by_value_1/MinimumMinimumq_dense/add_5:z:0*q_dense/clip_by_value_1/Minimum/y:output:0*
T0*
_output_shapes
: ^
q_dense/clip_by_value_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *  Ε
q_dense/clip_by_value_1Maximum#q_dense/clip_by_value_1/Minimum:z:0"q_dense/clip_by_value_1/y:output:0*
T0*
_output_shapes
: j
q_dense/mul_5Mulq_dense/Cast_1:y:0q_dense/clip_by_value_1:z:0*
T0*
_output_shapes
: X
q_dense/truediv_3/yConst*
_output_shapes
: *
dtype0*
valueB
 *  Er
q_dense/truediv_3RealDivq_dense/mul_5:z:0q_dense/truediv_3/y:output:0*
T0*
_output_shapes
: T
q_dense/mul_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?j
q_dense/mul_6Mulq_dense/mul_6/x:output:0q_dense/truediv_3:z:0*
T0*
_output_shapes
: v
q_dense/ReadVariableOp_4ReadVariableOp!q_dense_readvariableop_3_resource*
_output_shapes
: *
dtype0[
q_dense/Neg_3Neg q_dense/ReadVariableOp_4:value:0*
T0*
_output_shapes
: a
q_dense/add_6AddV2q_dense/Neg_3:y:0q_dense/mul_6:z:0*
T0*
_output_shapes
: T
q_dense/mul_7/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?f
q_dense/mul_7Mulq_dense/mul_7/x:output:0q_dense/add_6:z:0*
T0*
_output_shapes
: ^
q_dense/StopGradient_3StopGradientq_dense/mul_7:z:0*
T0*
_output_shapes
: v
q_dense/ReadVariableOp_5ReadVariableOp!q_dense_readvariableop_3_resource*
_output_shapes
: *
dtype0~
q_dense/add_7AddV2 q_dense/ReadVariableOp_5:value:0q_dense/StopGradient_3:output:0*
T0*
_output_shapes
: y
q_dense/BiasAddBiasAddq_dense/MatMul:product:0q_dense/add_7:z:0*
T0*'
_output_shapes
:????????? Q
q_dense/Pow_2/xConst*
_output_shapes
: *
dtype0*
value	B :Q
q_dense/Pow_2/yConst*
_output_shapes
: *
dtype0*
value	B :i
q_dense/Pow_2Powq_dense/Pow_2/x:output:0q_dense/Pow_2/y:output:0*
T0*
_output_shapes
: Y
q_dense/Cast_2Castq_dense/Pow_2:z:0*

DstT0*

SrcT0*
_output_shapes
: Q
q_dense/Pow_3/xConst*
_output_shapes
: *
dtype0*
value	B :Q
q_dense/Pow_3/yConst*
_output_shapes
: *
dtype0*
value	B :i
q_dense/Pow_3Powq_dense/Pow_3/x:output:0q_dense/Pow_3/y:output:0*
T0*
_output_shapes
: Y
q_dense/Cast_3Castq_dense/Pow_3:z:0*

DstT0*

SrcT0*
_output_shapes
: R
q_dense/ConstConst*
_output_shapes
: *
dtype0*
valueB
 *   @R
q_dense/Cast_4/xConst*
_output_shapes
: *
dtype0*
value	B :a
q_dense/Cast_4Castq_dense/Cast_4/x:output:0*

DstT0*

SrcT0*
_output_shapes
: R
q_dense/sub/yConst*
_output_shapes
: *
dtype0*
valueB
 *  PA_
q_dense/subSubq_dense/Cast_4:y:0q_dense/sub/y:output:0*
T0*
_output_shapes
: ^
q_dense/Pow_4Powq_dense/Const:output:0q_dense/sub:z:0*
T0*
_output_shapes
: \
q_dense/sub_1Subq_dense/Cast_3:y:0q_dense/Pow_4:z:0*
T0*
_output_shapes
: }
q_dense/LessEqual	LessEqualq_dense/BiasAdd:output:0q_dense/sub_1:z:0*
T0*'
_output_shapes
:????????? `
q_dense/ReluReluq_dense/BiasAdd:output:0*
T0*'
_output_shapes
:????????? _
q_dense/ones_like/ShapeShapeq_dense/BiasAdd:output:0*
T0*
_output_shapes
:\
q_dense/ones_like/ConstConst*
_output_shapes
: *
dtype0*
valueB
 *  ?
q_dense/ones_likeFill q_dense/ones_like/Shape:output:0 q_dense/ones_like/Const:output:0*
T0*'
_output_shapes
:????????? \
q_dense/sub_2Subq_dense/Cast_3:y:0q_dense/Pow_4:z:0*
T0*
_output_shapes
: u
q_dense/mul_8Mulq_dense/ones_like:output:0q_dense/sub_2:z:0*
T0*'
_output_shapes
:????????? 
q_dense/SelectV2SelectV2q_dense/LessEqual:z:0q_dense/Relu:activations:0q_dense/mul_8:z:0*
T0*'
_output_shapes
:????????? t
q_dense/mul_9Mulq_dense/BiasAdd:output:0q_dense/Cast_2:y:0*
T0*'
_output_shapes
:????????? u
q_dense/truediv_4RealDivq_dense/mul_9:z:0q_dense/Cast_3:y:0*
T0*'
_output_shapes
:????????? ]
q_dense/Neg_4Negq_dense/truediv_4:z:0*
T0*'
_output_shapes
:????????? a
q_dense/Round_2Roundq_dense/truediv_4:z:0*
T0*'
_output_shapes
:????????? p
q_dense/add_8AddV2q_dense/Neg_4:y:0q_dense/Round_2:y:0*
T0*'
_output_shapes
:????????? k
q_dense/StopGradient_4StopGradientq_dense/add_8:z:0*
T0*'
_output_shapes
:????????? 
q_dense/add_9AddV2q_dense/truediv_4:z:0q_dense/StopGradient_4:output:0*
T0*'
_output_shapes
:????????? u
q_dense/truediv_5RealDivq_dense/add_9:z:0q_dense/Cast_2:y:0*
T0*'
_output_shapes
:????????? X
q_dense/truediv_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?o
q_dense/truediv_6RealDivq_dense/truediv_6/x:output:0q_dense/Cast_2:y:0*
T0*
_output_shapes
: T
q_dense/sub_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?f
q_dense/sub_3Subq_dense/sub_3/x:output:0q_dense/truediv_6:z:0*
T0*
_output_shapes
: 
q_dense/clip_by_value_2/MinimumMinimumq_dense/truediv_5:z:0q_dense/sub_3:z:0*
T0*'
_output_shapes
:????????? ^
q_dense/clip_by_value_2/yConst*
_output_shapes
: *
dtype0*
valueB
 *    
q_dense/clip_by_value_2Maximum#q_dense/clip_by_value_2/Minimum:z:0"q_dense/clip_by_value_2/y:output:0*
T0*'
_output_shapes
:????????? x
q_dense/mul_10Mulq_dense/Cast_3:y:0q_dense/clip_by_value_2:z:0*
T0*'
_output_shapes
:????????? a
q_dense/Neg_5Negq_dense/SelectV2:output:0*
T0*'
_output_shapes
:????????? p
q_dense/add_10AddV2q_dense/Neg_5:y:0q_dense/mul_10:z:0*
T0*'
_output_shapes
:????????? U
q_dense/mul_11/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?v
q_dense/mul_11Mulq_dense/mul_11/x:output:0q_dense/add_10:z:0*
T0*'
_output_shapes
:????????? l
q_dense/StopGradient_5StopGradientq_dense/mul_11:z:0*
T0*'
_output_shapes
:????????? 
q_dense/add_11AddV2q_dense/SelectV2:output:0q_dense/StopGradient_5:output:0*
T0*'
_output_shapes
:????????? Q
q_dense_1/Pow/xConst*
_output_shapes
: *
dtype0*
value	B :Q
q_dense_1/Pow/yConst*
_output_shapes
: *
dtype0*
value	B :i
q_dense_1/PowPowq_dense_1/Pow/x:output:0q_dense_1/Pow/y:output:0*
T0*
_output_shapes
: Y
q_dense_1/CastCastq_dense_1/Pow:z:0*

DstT0*

SrcT0*
_output_shapes
: z
q_dense_1/ReadVariableOpReadVariableOp!q_dense_1_readvariableop_resource*
_output_shapes

: *
dtype0T
q_dense_1/mul/yConst*
_output_shapes
: *
dtype0*
valueB
 *   By
q_dense_1/mulMul q_dense_1/ReadVariableOp:value:0q_dense_1/mul/y:output:0*
T0*
_output_shapes

: l
q_dense_1/truedivRealDivq_dense_1/mul:z:0q_dense_1/Cast:y:0*
T0*
_output_shapes

: T
q_dense_1/NegNegq_dense_1/truediv:z:0*
T0*
_output_shapes

: X
q_dense_1/RoundRoundq_dense_1/truediv:z:0*
T0*
_output_shapes

: g
q_dense_1/addAddV2q_dense_1/Neg:y:0q_dense_1/Round:y:0*
T0*
_output_shapes

: b
q_dense_1/StopGradientStopGradientq_dense_1/add:z:0*
T0*
_output_shapes

: y
q_dense_1/add_1AddV2q_dense_1/truediv:z:0q_dense_1/StopGradient:output:0*
T0*
_output_shapes

: f
!q_dense_1/clip_by_value/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 *  ψA
q_dense_1/clip_by_value/MinimumMinimumq_dense_1/add_1:z:0*q_dense_1/clip_by_value/Minimum/y:output:0*
T0*
_output_shapes

: ^
q_dense_1/clip_by_value/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Β
q_dense_1/clip_by_valueMaximum#q_dense_1/clip_by_value/Minimum:z:0"q_dense_1/clip_by_value/y:output:0*
T0*
_output_shapes

: p
q_dense_1/mul_1Mulq_dense_1/Cast:y:0q_dense_1/clip_by_value:z:0*
T0*
_output_shapes

: Z
q_dense_1/truediv_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   B|
q_dense_1/truediv_1RealDivq_dense_1/mul_1:z:0q_dense_1/truediv_1/y:output:0*
T0*
_output_shapes

: V
q_dense_1/mul_2/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?t
q_dense_1/mul_2Mulq_dense_1/mul_2/x:output:0q_dense_1/truediv_1:z:0*
T0*
_output_shapes

: |
q_dense_1/ReadVariableOp_1ReadVariableOp!q_dense_1_readvariableop_resource*
_output_shapes

: *
dtype0c
q_dense_1/Neg_1Neg"q_dense_1/ReadVariableOp_1:value:0*
T0*
_output_shapes

: k
q_dense_1/add_2AddV2q_dense_1/Neg_1:y:0q_dense_1/mul_2:z:0*
T0*
_output_shapes

: V
q_dense_1/mul_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?p
q_dense_1/mul_3Mulq_dense_1/mul_3/x:output:0q_dense_1/add_2:z:0*
T0*
_output_shapes

: f
q_dense_1/StopGradient_1StopGradientq_dense_1/mul_3:z:0*
T0*
_output_shapes

: |
q_dense_1/ReadVariableOp_2ReadVariableOp!q_dense_1_readvariableop_resource*
_output_shapes

: *
dtype0
q_dense_1/add_3AddV2"q_dense_1/ReadVariableOp_2:value:0!q_dense_1/StopGradient_1:output:0*
T0*
_output_shapes

: u
q_dense_1/MatMulMatMulq_dense/add_11:z:0q_dense_1/add_3:z:0*
T0*'
_output_shapes
:?????????S
q_dense_1/Pow_1/xConst*
_output_shapes
: *
dtype0*
value	B :S
q_dense_1/Pow_1/yConst*
_output_shapes
: *
dtype0*
value	B :o
q_dense_1/Pow_1Powq_dense_1/Pow_1/x:output:0q_dense_1/Pow_1/y:output:0*
T0*
_output_shapes
: ]
q_dense_1/Cast_1Castq_dense_1/Pow_1:z:0*

DstT0*

SrcT0*
_output_shapes
: z
q_dense_1/ReadVariableOp_3ReadVariableOp#q_dense_1_readvariableop_3_resource*
_output_shapes
:*
dtype0V
q_dense_1/mul_4/yConst*
_output_shapes
: *
dtype0*
valueB
 *  E{
q_dense_1/mul_4Mul"q_dense_1/ReadVariableOp_3:value:0q_dense_1/mul_4/y:output:0*
T0*
_output_shapes
:n
q_dense_1/truediv_2RealDivq_dense_1/mul_4:z:0q_dense_1/Cast_1:y:0*
T0*
_output_shapes
:T
q_dense_1/Neg_2Negq_dense_1/truediv_2:z:0*
T0*
_output_shapes
:X
q_dense_1/Round_1Roundq_dense_1/truediv_2:z:0*
T0*
_output_shapes
:i
q_dense_1/add_4AddV2q_dense_1/Neg_2:y:0q_dense_1/Round_1:y:0*
T0*
_output_shapes
:b
q_dense_1/StopGradient_2StopGradientq_dense_1/add_4:z:0*
T0*
_output_shapes
:y
q_dense_1/add_5AddV2q_dense_1/truediv_2:z:0!q_dense_1/StopGradient_2:output:0*
T0*
_output_shapes
:h
#q_dense_1/clip_by_value_1/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * πE
!q_dense_1/clip_by_value_1/MinimumMinimumq_dense_1/add_5:z:0,q_dense_1/clip_by_value_1/Minimum/y:output:0*
T0*
_output_shapes
:`
q_dense_1/clip_by_value_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *  Ε
q_dense_1/clip_by_value_1Maximum%q_dense_1/clip_by_value_1/Minimum:z:0$q_dense_1/clip_by_value_1/y:output:0*
T0*
_output_shapes
:p
q_dense_1/mul_5Mulq_dense_1/Cast_1:y:0q_dense_1/clip_by_value_1:z:0*
T0*
_output_shapes
:Z
q_dense_1/truediv_3/yConst*
_output_shapes
: *
dtype0*
valueB
 *  Ex
q_dense_1/truediv_3RealDivq_dense_1/mul_5:z:0q_dense_1/truediv_3/y:output:0*
T0*
_output_shapes
:V
q_dense_1/mul_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?p
q_dense_1/mul_6Mulq_dense_1/mul_6/x:output:0q_dense_1/truediv_3:z:0*
T0*
_output_shapes
:z
q_dense_1/ReadVariableOp_4ReadVariableOp#q_dense_1_readvariableop_3_resource*
_output_shapes
:*
dtype0_
q_dense_1/Neg_3Neg"q_dense_1/ReadVariableOp_4:value:0*
T0*
_output_shapes
:g
q_dense_1/add_6AddV2q_dense_1/Neg_3:y:0q_dense_1/mul_6:z:0*
T0*
_output_shapes
:V
q_dense_1/mul_7/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?l
q_dense_1/mul_7Mulq_dense_1/mul_7/x:output:0q_dense_1/add_6:z:0*
T0*
_output_shapes
:b
q_dense_1/StopGradient_3StopGradientq_dense_1/mul_7:z:0*
T0*
_output_shapes
:z
q_dense_1/ReadVariableOp_5ReadVariableOp#q_dense_1_readvariableop_3_resource*
_output_shapes
:*
dtype0
q_dense_1/add_7AddV2"q_dense_1/ReadVariableOp_5:value:0!q_dense_1/StopGradient_3:output:0*
T0*
_output_shapes
:
q_dense_1/BiasAddBiasAddq_dense_1/MatMul:product:0q_dense_1/add_7:z:0*
T0*'
_output_shapes
:?????????S
q_dense_1/Pow_2/xConst*
_output_shapes
: *
dtype0*
value	B :S
q_dense_1/Pow_2/yConst*
_output_shapes
: *
dtype0*
value	B :o
q_dense_1/Pow_2Powq_dense_1/Pow_2/x:output:0q_dense_1/Pow_2/y:output:0*
T0*
_output_shapes
: ]
q_dense_1/Cast_2Castq_dense_1/Pow_2:z:0*

DstT0*

SrcT0*
_output_shapes
: S
q_dense_1/Pow_3/xConst*
_output_shapes
: *
dtype0*
value	B :S
q_dense_1/Pow_3/yConst*
_output_shapes
: *
dtype0*
value	B :o
q_dense_1/Pow_3Powq_dense_1/Pow_3/x:output:0q_dense_1/Pow_3/y:output:0*
T0*
_output_shapes
: ]
q_dense_1/Cast_3Castq_dense_1/Pow_3:z:0*

DstT0*

SrcT0*
_output_shapes
: T
q_dense_1/ConstConst*
_output_shapes
: *
dtype0*
valueB
 *   @T
q_dense_1/Cast_4/xConst*
_output_shapes
: *
dtype0*
value	B :e
q_dense_1/Cast_4Castq_dense_1/Cast_4/x:output:0*

DstT0*

SrcT0*
_output_shapes
: T
q_dense_1/sub/yConst*
_output_shapes
: *
dtype0*
valueB
 *  PAe
q_dense_1/subSubq_dense_1/Cast_4:y:0q_dense_1/sub/y:output:0*
T0*
_output_shapes
: d
q_dense_1/Pow_4Powq_dense_1/Const:output:0q_dense_1/sub:z:0*
T0*
_output_shapes
: b
q_dense_1/sub_1Subq_dense_1/Cast_3:y:0q_dense_1/Pow_4:z:0*
T0*
_output_shapes
: 
q_dense_1/LessEqual	LessEqualq_dense_1/BiasAdd:output:0q_dense_1/sub_1:z:0*
T0*'
_output_shapes
:?????????d
q_dense_1/ReluReluq_dense_1/BiasAdd:output:0*
T0*'
_output_shapes
:?????????c
q_dense_1/ones_like/ShapeShapeq_dense_1/BiasAdd:output:0*
T0*
_output_shapes
:^
q_dense_1/ones_like/ConstConst*
_output_shapes
: *
dtype0*
valueB
 *  ?
q_dense_1/ones_likeFill"q_dense_1/ones_like/Shape:output:0"q_dense_1/ones_like/Const:output:0*
T0*'
_output_shapes
:?????????b
q_dense_1/sub_2Subq_dense_1/Cast_3:y:0q_dense_1/Pow_4:z:0*
T0*
_output_shapes
: {
q_dense_1/mul_8Mulq_dense_1/ones_like:output:0q_dense_1/sub_2:z:0*
T0*'
_output_shapes
:?????????
q_dense_1/SelectV2SelectV2q_dense_1/LessEqual:z:0q_dense_1/Relu:activations:0q_dense_1/mul_8:z:0*
T0*'
_output_shapes
:?????????z
q_dense_1/mul_9Mulq_dense_1/BiasAdd:output:0q_dense_1/Cast_2:y:0*
T0*'
_output_shapes
:?????????{
q_dense_1/truediv_4RealDivq_dense_1/mul_9:z:0q_dense_1/Cast_3:y:0*
T0*'
_output_shapes
:?????????a
q_dense_1/Neg_4Negq_dense_1/truediv_4:z:0*
T0*'
_output_shapes
:?????????e
q_dense_1/Round_2Roundq_dense_1/truediv_4:z:0*
T0*'
_output_shapes
:?????????v
q_dense_1/add_8AddV2q_dense_1/Neg_4:y:0q_dense_1/Round_2:y:0*
T0*'
_output_shapes
:?????????o
q_dense_1/StopGradient_4StopGradientq_dense_1/add_8:z:0*
T0*'
_output_shapes
:?????????
q_dense_1/add_9AddV2q_dense_1/truediv_4:z:0!q_dense_1/StopGradient_4:output:0*
T0*'
_output_shapes
:?????????{
q_dense_1/truediv_5RealDivq_dense_1/add_9:z:0q_dense_1/Cast_2:y:0*
T0*'
_output_shapes
:?????????Z
q_dense_1/truediv_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?u
q_dense_1/truediv_6RealDivq_dense_1/truediv_6/x:output:0q_dense_1/Cast_2:y:0*
T0*
_output_shapes
: V
q_dense_1/sub_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?l
q_dense_1/sub_3Subq_dense_1/sub_3/x:output:0q_dense_1/truediv_6:z:0*
T0*
_output_shapes
: 
!q_dense_1/clip_by_value_2/MinimumMinimumq_dense_1/truediv_5:z:0q_dense_1/sub_3:z:0*
T0*'
_output_shapes
:?????????`
q_dense_1/clip_by_value_2/yConst*
_output_shapes
: *
dtype0*
valueB
 *    £
q_dense_1/clip_by_value_2Maximum%q_dense_1/clip_by_value_2/Minimum:z:0$q_dense_1/clip_by_value_2/y:output:0*
T0*'
_output_shapes
:?????????~
q_dense_1/mul_10Mulq_dense_1/Cast_3:y:0q_dense_1/clip_by_value_2:z:0*
T0*'
_output_shapes
:?????????e
q_dense_1/Neg_5Negq_dense_1/SelectV2:output:0*
T0*'
_output_shapes
:?????????v
q_dense_1/add_10AddV2q_dense_1/Neg_5:y:0q_dense_1/mul_10:z:0*
T0*'
_output_shapes
:?????????W
q_dense_1/mul_11/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?|
q_dense_1/mul_11Mulq_dense_1/mul_11/x:output:0q_dense_1/add_10:z:0*
T0*'
_output_shapes
:?????????p
q_dense_1/StopGradient_5StopGradientq_dense_1/mul_11:z:0*
T0*'
_output_shapes
:?????????
q_dense_1/add_11AddV2q_dense_1/SelectV2:output:0!q_dense_1/StopGradient_5:output:0*
T0*'
_output_shapes
:?????????J
mu/Pow/xConst*
_output_shapes
: *
dtype0*
value	B :J
mu/Pow/yConst*
_output_shapes
: *
dtype0*
value	B :T
mu/PowPowmu/Pow/x:output:0mu/Pow/y:output:0*
T0*
_output_shapes
: K
mu/CastCast
mu/Pow:z:0*

DstT0*

SrcT0*
_output_shapes
: l
mu/ReadVariableOpReadVariableOpmu_readvariableop_resource*
_output_shapes

:*
dtype0M
mu/mul/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Bd
mu/mulMulmu/ReadVariableOp:value:0mu/mul/y:output:0*
T0*
_output_shapes

:W

mu/truedivRealDiv
mu/mul:z:0mu/Cast:y:0*
T0*
_output_shapes

:F
mu/NegNegmu/truediv:z:0*
T0*
_output_shapes

:J
mu/RoundRoundmu/truediv:z:0*
T0*
_output_shapes

:R
mu/addAddV2
mu/Neg:y:0mu/Round:y:0*
T0*
_output_shapes

:T
mu/StopGradientStopGradient
mu/add:z:0*
T0*
_output_shapes

:d
mu/add_1AddV2mu/truediv:z:0mu/StopGradient:output:0*
T0*
_output_shapes

:_
mu/clip_by_value/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 *  ψA
mu/clip_by_value/MinimumMinimummu/add_1:z:0#mu/clip_by_value/Minimum/y:output:0*
T0*
_output_shapes

:W
mu/clip_by_value/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Β
mu/clip_by_valueMaximummu/clip_by_value/Minimum:z:0mu/clip_by_value/y:output:0*
T0*
_output_shapes

:[
mu/mul_1Mulmu/Cast:y:0mu/clip_by_value:z:0*
T0*
_output_shapes

:S
mu/truediv_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Bg
mu/truediv_1RealDivmu/mul_1:z:0mu/truediv_1/y:output:0*
T0*
_output_shapes

:O

mu/mul_2/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?_
mu/mul_2Mulmu/mul_2/x:output:0mu/truediv_1:z:0*
T0*
_output_shapes

:n
mu/ReadVariableOp_1ReadVariableOpmu_readvariableop_resource*
_output_shapes

:*
dtype0U
mu/Neg_1Negmu/ReadVariableOp_1:value:0*
T0*
_output_shapes

:V
mu/add_2AddV2mu/Neg_1:y:0mu/mul_2:z:0*
T0*
_output_shapes

:O

mu/mul_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?[
mu/mul_3Mulmu/mul_3/x:output:0mu/add_2:z:0*
T0*
_output_shapes

:X
mu/StopGradient_1StopGradientmu/mul_3:z:0*
T0*
_output_shapes

:n
mu/ReadVariableOp_2ReadVariableOpmu_readvariableop_resource*
_output_shapes

:*
dtype0s
mu/add_3AddV2mu/ReadVariableOp_2:value:0mu/StopGradient_1:output:0*
T0*
_output_shapes

:i
	mu/MatMulMatMulq_dense_1/add_11:z:0mu/add_3:z:0*
T0*'
_output_shapes
:?????????L

mu/Pow_1/xConst*
_output_shapes
: *
dtype0*
value	B :L

mu/Pow_1/yConst*
_output_shapes
: *
dtype0*
value	B :Z
mu/Pow_1Powmu/Pow_1/x:output:0mu/Pow_1/y:output:0*
T0*
_output_shapes
: O
	mu/Cast_1Castmu/Pow_1:z:0*

DstT0*

SrcT0*
_output_shapes
: l
mu/ReadVariableOp_3ReadVariableOpmu_readvariableop_3_resource*
_output_shapes
:*
dtype0O

mu/mul_4/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Df
mu/mul_4Mulmu/ReadVariableOp_3:value:0mu/mul_4/y:output:0*
T0*
_output_shapes
:Y
mu/truediv_2RealDivmu/mul_4:z:0mu/Cast_1:y:0*
T0*
_output_shapes
:F
mu/Neg_2Negmu/truediv_2:z:0*
T0*
_output_shapes
:J

mu/Round_1Roundmu/truediv_2:z:0*
T0*
_output_shapes
:T
mu/add_4AddV2mu/Neg_2:y:0mu/Round_1:y:0*
T0*
_output_shapes
:T
mu/StopGradient_2StopGradientmu/add_4:z:0*
T0*
_output_shapes
:d
mu/add_5AddV2mu/truediv_2:z:0mu/StopGradient_2:output:0*
T0*
_output_shapes
:a
mu/clip_by_value_1/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * ?C
mu/clip_by_value_1/MinimumMinimummu/add_5:z:0%mu/clip_by_value_1/Minimum/y:output:0*
T0*
_output_shapes
:Y
mu/clip_by_value_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Δ
mu/clip_by_value_1Maximummu/clip_by_value_1/Minimum:z:0mu/clip_by_value_1/y:output:0*
T0*
_output_shapes
:[
mu/mul_5Mulmu/Cast_1:y:0mu/clip_by_value_1:z:0*
T0*
_output_shapes
:S
mu/truediv_3/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Dc
mu/truediv_3RealDivmu/mul_5:z:0mu/truediv_3/y:output:0*
T0*
_output_shapes
:O

mu/mul_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?[
mu/mul_6Mulmu/mul_6/x:output:0mu/truediv_3:z:0*
T0*
_output_shapes
:l
mu/ReadVariableOp_4ReadVariableOpmu_readvariableop_3_resource*
_output_shapes
:*
dtype0Q
mu/Neg_3Negmu/ReadVariableOp_4:value:0*
T0*
_output_shapes
:R
mu/add_6AddV2mu/Neg_3:y:0mu/mul_6:z:0*
T0*
_output_shapes
:O

mu/mul_7/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?W
mu/mul_7Mulmu/mul_7/x:output:0mu/add_6:z:0*
T0*
_output_shapes
:T
mu/StopGradient_3StopGradientmu/mul_7:z:0*
T0*
_output_shapes
:l
mu/ReadVariableOp_5ReadVariableOpmu_readvariableop_3_resource*
_output_shapes
:*
dtype0o
mu/add_7AddV2mu/ReadVariableOp_5:value:0mu/StopGradient_3:output:0*
T0*
_output_shapes
:j

mu/BiasAddBiasAddmu/MatMul:product:0mu/add_7:z:0*
T0*'
_output_shapes
:?????????L

mu/Pow_2/xConst*
_output_shapes
: *
dtype0*
value	B :L

mu/Pow_2/yConst*
_output_shapes
: *
dtype0*
value	B :Z
mu/Pow_2Powmu/Pow_2/x:output:0mu/Pow_2/y:output:0*
T0*
_output_shapes
: O
	mu/Cast_2Castmu/Pow_2:z:0*

DstT0*

SrcT0*
_output_shapes
: O

mu/mul_8/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Dk
mu/mul_8Mulmu/BiasAdd:output:0mu/mul_8/y:output:0*
T0*'
_output_shapes
:?????????f
mu/truediv_4RealDivmu/mul_8:z:0mu/Cast_2:y:0*
T0*'
_output_shapes
:?????????S
mu/Neg_4Negmu/truediv_4:z:0*
T0*'
_output_shapes
:?????????W

mu/Round_2Roundmu/truediv_4:z:0*
T0*'
_output_shapes
:?????????a
mu/add_8AddV2mu/Neg_4:y:0mu/Round_2:y:0*
T0*'
_output_shapes
:?????????a
mu/StopGradient_4StopGradientmu/add_8:z:0*
T0*'
_output_shapes
:?????????q
mu/add_9AddV2mu/truediv_4:z:0mu/StopGradient_4:output:0*
T0*'
_output_shapes
:?????????a
mu/clip_by_value_2/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * ?C
mu/clip_by_value_2/MinimumMinimummu/add_9:z:0%mu/clip_by_value_2/Minimum/y:output:0*
T0*'
_output_shapes
:?????????Y
mu/clip_by_value_2/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Δ
mu/clip_by_value_2Maximummu/clip_by_value_2/Minimum:z:0mu/clip_by_value_2/y:output:0*
T0*'
_output_shapes
:?????????h
mu/mul_9Mulmu/Cast_2:y:0mu/clip_by_value_2:z:0*
T0*'
_output_shapes
:?????????S
mu/truediv_5/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Dp
mu/truediv_5RealDivmu/mul_9:z:0mu/truediv_5/y:output:0*
T0*'
_output_shapes
:?????????P
mu/mul_10/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?j
	mu/mul_10Mulmu/mul_10/x:output:0mu/truediv_5:z:0*
T0*'
_output_shapes
:?????????V
mu/Neg_5Negmu/BiasAdd:output:0*
T0*'
_output_shapes
:?????????a
	mu/add_10AddV2mu/Neg_5:y:0mu/mul_10:z:0*
T0*'
_output_shapes
:?????????P
mu/mul_11/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?g
	mu/mul_11Mulmu/mul_11/x:output:0mu/add_10:z:0*
T0*'
_output_shapes
:?????????b
mu/StopGradient_5StopGradientmu/mul_11:z:0*
T0*'
_output_shapes
:?????????u
	mu/add_11AddV2mu/BiasAdd:output:0mu/StopGradient_5:output:0*
T0*'
_output_shapes
:?????????
-q_dense/kernel/Regularizer/Abs/ReadVariableOpReadVariableOpq_dense_readvariableop_resource*
_output_shapes

:9 *
dtype0
q_dense/kernel/Regularizer/AbsAbs5q_dense/kernel/Regularizer/Abs/ReadVariableOp:value:0*
T0*
_output_shapes

:9 q
 q_dense/kernel/Regularizer/ConstConst*
_output_shapes
:*
dtype0*
valueB"       
q_dense/kernel/Regularizer/SumSum"q_dense/kernel/Regularizer/Abs:y:0)q_dense/kernel/Regularizer/Const:output:0*
T0*
_output_shapes
: e
 q_dense/kernel/Regularizer/mul/xConst*
_output_shapes
: *
dtype0*
valueB
 *o:
q_dense/kernel/Regularizer/mulMul)q_dense/kernel/Regularizer/mul/x:output:0'q_dense/kernel/Regularizer/Sum:output:0*
T0*
_output_shapes
: 
/q_dense_1/kernel/Regularizer/Abs/ReadVariableOpReadVariableOp!q_dense_1_readvariableop_resource*
_output_shapes

: *
dtype0
 q_dense_1/kernel/Regularizer/AbsAbs7q_dense_1/kernel/Regularizer/Abs/ReadVariableOp:value:0*
T0*
_output_shapes

: s
"q_dense_1/kernel/Regularizer/ConstConst*
_output_shapes
:*
dtype0*
valueB"       
 q_dense_1/kernel/Regularizer/SumSum$q_dense_1/kernel/Regularizer/Abs:y:0+q_dense_1/kernel/Regularizer/Const:output:0*
T0*
_output_shapes
: g
"q_dense_1/kernel/Regularizer/mul/xConst*
_output_shapes
: *
dtype0*
valueB
 *     
 q_dense_1/kernel/Regularizer/mulMul+q_dense_1/kernel/Regularizer/mul/x:output:0)q_dense_1/kernel/Regularizer/Sum:output:0*
T0*
_output_shapes
: \
IdentityIdentitymu/add_11:z:0^NoOp*
T0*'
_output_shapes
:?????????φ
NoOpNoOp^mu/ReadVariableOp^mu/ReadVariableOp_1^mu/ReadVariableOp_2^mu/ReadVariableOp_3^mu/ReadVariableOp_4^mu/ReadVariableOp_5^q_dense/ReadVariableOp^q_dense/ReadVariableOp_1^q_dense/ReadVariableOp_2^q_dense/ReadVariableOp_3^q_dense/ReadVariableOp_4^q_dense/ReadVariableOp_5.^q_dense/kernel/Regularizer/Abs/ReadVariableOp^q_dense_1/ReadVariableOp^q_dense_1/ReadVariableOp_1^q_dense_1/ReadVariableOp_2^q_dense_1/ReadVariableOp_3^q_dense_1/ReadVariableOp_4^q_dense_1/ReadVariableOp_50^q_dense_1/kernel/Regularizer/Abs/ReadVariableOp*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime*2
_input_shapes!
:?????????9: : : : : : 2&
mu/ReadVariableOpmu/ReadVariableOp2*
mu/ReadVariableOp_1mu/ReadVariableOp_12*
mu/ReadVariableOp_2mu/ReadVariableOp_22*
mu/ReadVariableOp_3mu/ReadVariableOp_32*
mu/ReadVariableOp_4mu/ReadVariableOp_42*
mu/ReadVariableOp_5mu/ReadVariableOp_520
q_dense/ReadVariableOpq_dense/ReadVariableOp24
q_dense/ReadVariableOp_1q_dense/ReadVariableOp_124
q_dense/ReadVariableOp_2q_dense/ReadVariableOp_224
q_dense/ReadVariableOp_3q_dense/ReadVariableOp_324
q_dense/ReadVariableOp_4q_dense/ReadVariableOp_424
q_dense/ReadVariableOp_5q_dense/ReadVariableOp_52^
-q_dense/kernel/Regularizer/Abs/ReadVariableOp-q_dense/kernel/Regularizer/Abs/ReadVariableOp24
q_dense_1/ReadVariableOpq_dense_1/ReadVariableOp28
q_dense_1/ReadVariableOp_1q_dense_1/ReadVariableOp_128
q_dense_1/ReadVariableOp_2q_dense_1/ReadVariableOp_228
q_dense_1/ReadVariableOp_3q_dense_1/ReadVariableOp_328
q_dense_1/ReadVariableOp_4q_dense_1/ReadVariableOp_428
q_dense_1/ReadVariableOp_5q_dense_1/ReadVariableOp_52b
/q_dense_1/kernel/Regularizer/Abs/ReadVariableOp/q_dense_1/kernel/Regularizer/Abs/ReadVariableOp:O K
'
_output_shapes
:?????????9
 
_user_specified_nameinputs
έX
Ψ
C__inference_q_dense_1_layer_call_and_return_conditional_losses_2450

inputs)
readvariableop_resource: '
readvariableop_3_resource:
identity’ReadVariableOp’ReadVariableOp_1’ReadVariableOp_2’ReadVariableOp_3’ReadVariableOp_4’ReadVariableOp_5’/q_dense_1/kernel/Regularizer/Abs/ReadVariableOpG
Pow/xConst*
_output_shapes
: *
dtype0*
value	B :G
Pow/yConst*
_output_shapes
: *
dtype0*
value	B :K
PowPowPow/x:output:0Pow/y:output:0*
T0*
_output_shapes
: E
CastCastPow:z:0*

DstT0*

SrcT0*
_output_shapes
: f
ReadVariableOpReadVariableOpreadvariableop_resource*
_output_shapes

: *
dtype0J
mul/yConst*
_output_shapes
: *
dtype0*
valueB
 *   B[
mulMulReadVariableOp:value:0mul/y:output:0*
T0*
_output_shapes

: N
truedivRealDivmul:z:0Cast:y:0*
T0*
_output_shapes

: @
NegNegtruediv:z:0*
T0*
_output_shapes

: D
RoundRoundtruediv:z:0*
T0*
_output_shapes

: I
addAddV2Neg:y:0	Round:y:0*
T0*
_output_shapes

: N
StopGradientStopGradientadd:z:0*
T0*
_output_shapes

: [
add_1AddV2truediv:z:0StopGradient:output:0*
T0*
_output_shapes

: \
clip_by_value/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 *  ψAv
clip_by_value/MinimumMinimum	add_1:z:0 clip_by_value/Minimum/y:output:0*
T0*
_output_shapes

: T
clip_by_value/yConst*
_output_shapes
: *
dtype0*
valueB
 *   Βv
clip_by_valueMaximumclip_by_value/Minimum:z:0clip_by_value/y:output:0*
T0*
_output_shapes

: R
mul_1MulCast:y:0clip_by_value:z:0*
T0*
_output_shapes

: P
truediv_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *   B^
	truediv_1RealDiv	mul_1:z:0truediv_1/y:output:0*
T0*
_output_shapes

: L
mul_2/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?V
mul_2Mulmul_2/x:output:0truediv_1:z:0*
T0*
_output_shapes

: h
ReadVariableOp_1ReadVariableOpreadvariableop_resource*
_output_shapes

: *
dtype0O
Neg_1NegReadVariableOp_1:value:0*
T0*
_output_shapes

: M
add_2AddV2	Neg_1:y:0	mul_2:z:0*
T0*
_output_shapes

: L
mul_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?R
mul_3Mulmul_3/x:output:0	add_2:z:0*
T0*
_output_shapes

: R
StopGradient_1StopGradient	mul_3:z:0*
T0*
_output_shapes

: h
ReadVariableOp_2ReadVariableOpreadvariableop_resource*
_output_shapes

: *
dtype0j
add_3AddV2ReadVariableOp_2:value:0StopGradient_1:output:0*
T0*
_output_shapes

: U
MatMulMatMulinputs	add_3:z:0*
T0*'
_output_shapes
:?????????I
Pow_1/xConst*
_output_shapes
: *
dtype0*
value	B :I
Pow_1/yConst*
_output_shapes
: *
dtype0*
value	B :Q
Pow_1PowPow_1/x:output:0Pow_1/y:output:0*
T0*
_output_shapes
: I
Cast_1Cast	Pow_1:z:0*

DstT0*

SrcT0*
_output_shapes
: f
ReadVariableOp_3ReadVariableOpreadvariableop_3_resource*
_output_shapes
:*
dtype0L
mul_4/yConst*
_output_shapes
: *
dtype0*
valueB
 *  E]
mul_4MulReadVariableOp_3:value:0mul_4/y:output:0*
T0*
_output_shapes
:P
	truediv_2RealDiv	mul_4:z:0
Cast_1:y:0*
T0*
_output_shapes
:@
Neg_2Negtruediv_2:z:0*
T0*
_output_shapes
:D
Round_1Roundtruediv_2:z:0*
T0*
_output_shapes
:K
add_4AddV2	Neg_2:y:0Round_1:y:0*
T0*
_output_shapes
:N
StopGradient_2StopGradient	add_4:z:0*
T0*
_output_shapes
:[
add_5AddV2truediv_2:z:0StopGradient_2:output:0*
T0*
_output_shapes
:^
clip_by_value_1/Minimum/yConst*
_output_shapes
: *
dtype0*
valueB
 * πEv
clip_by_value_1/MinimumMinimum	add_5:z:0"clip_by_value_1/Minimum/y:output:0*
T0*
_output_shapes
:V
clip_by_value_1/yConst*
_output_shapes
: *
dtype0*
valueB
 *  Εx
clip_by_value_1Maximumclip_by_value_1/Minimum:z:0clip_by_value_1/y:output:0*
T0*
_output_shapes
:R
mul_5Mul
Cast_1:y:0clip_by_value_1:z:0*
T0*
_output_shapes
:P
truediv_3/yConst*
_output_shapes
: *
dtype0*
valueB
 *  EZ
	truediv_3RealDiv	mul_5:z:0truediv_3/y:output:0*
T0*
_output_shapes
:L
mul_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?R
mul_6Mulmul_6/x:output:0truediv_3:z:0*
T0*
_output_shapes
:f
ReadVariableOp_4ReadVariableOpreadvariableop_3_resource*
_output_shapes
:*
dtype0K
Neg_3NegReadVariableOp_4:value:0*
T0*
_output_shapes
:I
add_6AddV2	Neg_3:y:0	mul_6:z:0*
T0*
_output_shapes
:L
mul_7/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?N
mul_7Mulmul_7/x:output:0	add_6:z:0*
T0*
_output_shapes
:N
StopGradient_3StopGradient	mul_7:z:0*
T0*
_output_shapes
:f
ReadVariableOp_5ReadVariableOpreadvariableop_3_resource*
_output_shapes
:*
dtype0f
add_7AddV2ReadVariableOp_5:value:0StopGradient_3:output:0*
T0*
_output_shapes
:a
BiasAddBiasAddMatMul:product:0	add_7:z:0*
T0*'
_output_shapes
:?????????I
Pow_2/xConst*
_output_shapes
: *
dtype0*
value	B :I
Pow_2/yConst*
_output_shapes
: *
dtype0*
value	B :Q
Pow_2PowPow_2/x:output:0Pow_2/y:output:0*
T0*
_output_shapes
: I
Cast_2Cast	Pow_2:z:0*

DstT0*

SrcT0*
_output_shapes
: I
Pow_3/xConst*
_output_shapes
: *
dtype0*
value	B :I
Pow_3/yConst*
_output_shapes
: *
dtype0*
value	B :Q
Pow_3PowPow_3/x:output:0Pow_3/y:output:0*
T0*
_output_shapes
: I
Cast_3Cast	Pow_3:z:0*

DstT0*

SrcT0*
_output_shapes
: J
ConstConst*
_output_shapes
: *
dtype0*
valueB
 *   @J
Cast_4/xConst*
_output_shapes
: *
dtype0*
value	B :Q
Cast_4CastCast_4/x:output:0*

DstT0*

SrcT0*
_output_shapes
: J
sub/yConst*
_output_shapes
: *
dtype0*
valueB
 *  PAG
subSub
Cast_4:y:0sub/y:output:0*
T0*
_output_shapes
: F
Pow_4PowConst:output:0sub:z:0*
T0*
_output_shapes
: D
sub_1Sub
Cast_3:y:0	Pow_4:z:0*
T0*
_output_shapes
: e
	LessEqual	LessEqualBiasAdd:output:0	sub_1:z:0*
T0*'
_output_shapes
:?????????P
ReluReluBiasAdd:output:0*
T0*'
_output_shapes
:?????????O
ones_like/ShapeShapeBiasAdd:output:0*
T0*
_output_shapes
:T
ones_like/ConstConst*
_output_shapes
: *
dtype0*
valueB
 *  ?w
	ones_likeFillones_like/Shape:output:0ones_like/Const:output:0*
T0*'
_output_shapes
:?????????D
sub_2Sub
Cast_3:y:0	Pow_4:z:0*
T0*
_output_shapes
: ]
mul_8Mulones_like:output:0	sub_2:z:0*
T0*'
_output_shapes
:?????????t
SelectV2SelectV2LessEqual:z:0Relu:activations:0	mul_8:z:0*
T0*'
_output_shapes
:?????????\
mul_9MulBiasAdd:output:0
Cast_2:y:0*
T0*'
_output_shapes
:?????????]
	truediv_4RealDiv	mul_9:z:0
Cast_3:y:0*
T0*'
_output_shapes
:?????????M
Neg_4Negtruediv_4:z:0*
T0*'
_output_shapes
:?????????Q
Round_2Roundtruediv_4:z:0*
T0*'
_output_shapes
:?????????X
add_8AddV2	Neg_4:y:0Round_2:y:0*
T0*'
_output_shapes
:?????????[
StopGradient_4StopGradient	add_8:z:0*
T0*'
_output_shapes
:?????????h
add_9AddV2truediv_4:z:0StopGradient_4:output:0*
T0*'
_output_shapes
:?????????]
	truediv_5RealDiv	add_9:z:0
Cast_2:y:0*
T0*'
_output_shapes
:?????????P
truediv_6/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?W
	truediv_6RealDivtruediv_6/x:output:0
Cast_2:y:0*
T0*
_output_shapes
: L
sub_3/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?N
sub_3Subsub_3/x:output:0truediv_6:z:0*
T0*
_output_shapes
: n
clip_by_value_2/MinimumMinimumtruediv_5:z:0	sub_3:z:0*
T0*'
_output_shapes
:?????????V
clip_by_value_2/yConst*
_output_shapes
: *
dtype0*
valueB
 *    
clip_by_value_2Maximumclip_by_value_2/Minimum:z:0clip_by_value_2/y:output:0*
T0*'
_output_shapes
:?????????`
mul_10Mul
Cast_3:y:0clip_by_value_2:z:0*
T0*'
_output_shapes
:?????????Q
Neg_5NegSelectV2:output:0*
T0*'
_output_shapes
:?????????X
add_10AddV2	Neg_5:y:0
mul_10:z:0*
T0*'
_output_shapes
:?????????M
mul_11/xConst*
_output_shapes
: *
dtype0*
valueB
 *  ?^
mul_11Mulmul_11/x:output:0
add_10:z:0*
T0*'
_output_shapes
:?????????\
StopGradient_5StopGradient
mul_11:z:0*
T0*'
_output_shapes
:?????????m
add_11AddV2SelectV2:output:0StopGradient_5:output:0*
T0*'
_output_shapes
:?????????
/q_dense_1/kernel/Regularizer/Abs/ReadVariableOpReadVariableOpreadvariableop_resource*
_output_shapes

: *
dtype0
 q_dense_1/kernel/Regularizer/AbsAbs7q_dense_1/kernel/Regularizer/Abs/ReadVariableOp:value:0*
T0*
_output_shapes

: s
"q_dense_1/kernel/Regularizer/ConstConst*
_output_shapes
:*
dtype0*
valueB"       
 q_dense_1/kernel/Regularizer/SumSum$q_dense_1/kernel/Regularizer/Abs:y:0+q_dense_1/kernel/Regularizer/Const:output:0*
T0*
_output_shapes
: g
"q_dense_1/kernel/Regularizer/mul/xConst*
_output_shapes
: *
dtype0*
valueB
 *     
 q_dense_1/kernel/Regularizer/mulMul+q_dense_1/kernel/Regularizer/mul/x:output:0)q_dense_1/kernel/Regularizer/Sum:output:0*
T0*
_output_shapes
: Y
IdentityIdentity
add_11:z:0^NoOp*
T0*'
_output_shapes
:?????????θ
NoOpNoOp^ReadVariableOp^ReadVariableOp_1^ReadVariableOp_2^ReadVariableOp_3^ReadVariableOp_4^ReadVariableOp_50^q_dense_1/kernel/Regularizer/Abs/ReadVariableOp*"
_acd_function_control_output(*
_output_shapes
 "
identityIdentity:output:0*(
_construction_contextkEagerRuntime**
_input_shapes
:????????? : : 2 
ReadVariableOpReadVariableOp2$
ReadVariableOp_1ReadVariableOp_12$
ReadVariableOp_2ReadVariableOp_22$
ReadVariableOp_3ReadVariableOp_32$
ReadVariableOp_4ReadVariableOp_42$
ReadVariableOp_5ReadVariableOp_52b
/q_dense_1/kernel/Regularizer/Abs/ReadVariableOp/q_dense_1/kernel/Regularizer/Abs/ReadVariableOp:O K
'
_output_shapes
:????????? 
 
_user_specified_nameinputs"΅	L
saver_filename:0StatefulPartitionedCall_1:0StatefulPartitionedCall_28"
saved_model_main_op

NoOp*>
__saved_model_init_op%#
__saved_model_init_op

NoOp*₯
serving_default
;
input_10
serving_default_input_1:0?????????96
mu0
StatefulPartitionedCall:0?????????tensorflow/serving/predict:§
γ
layer-0
layer-1
layer_with_weights-0
layer-2
layer_with_weights-1
layer-3
layer_with_weights-2
layer-4
	variables
trainable_variables
regularization_losses
		keras_api

__call__
*&call_and_return_all_conditional_losses
_default_save_signature

signatures"
_tf_keras_network
"
_tf_keras_input_layer
΄
	variables
trainable_variables
regularization_losses
	keras_api
__call__
*&call_and_return_all_conditional_losses
	quantizer"
_tf_keras_layer
Α
	variables
trainable_variables
regularization_losses
	keras_api
__call__
*&call_and_return_all_conditional_losses
kernel_quantizer
bias_quantizer
kernel_quantizer_internal
bias_quantizer_internal

quantizers

activation

 kernel
!bias"
_tf_keras_layer
Α
"	variables
#trainable_variables
$regularization_losses
%	keras_api
&__call__
*'&call_and_return_all_conditional_losses
(kernel_quantizer
)bias_quantizer
(kernel_quantizer_internal
*bias_quantizer_internal
+
quantizers
,
activation

-kernel
.bias"
_tf_keras_layer
Α
/	variables
0trainable_variables
1regularization_losses
2	keras_api
3__call__
*4&call_and_return_all_conditional_losses
5kernel_quantizer
6bias_quantizer
7kernel_quantizer_internal
8bias_quantizer_internal
9
quantizers
:
activation

;kernel
<bias"
_tf_keras_layer
J
 0
!1
-2
.3
;4
<5"
trackable_list_wrapper
J
 0
!1
-2
.3
;4
<5"
trackable_list_wrapper
.
=0
>1"
trackable_list_wrapper
Κ
?non_trainable_variables

@layers
Ametrics
Blayer_regularization_losses
Clayer_metrics
	variables
trainable_variables
regularization_losses

__call__
_default_save_signature
*&call_and_return_all_conditional_losses
&"call_and_return_conditional_losses"
_generic_user_object
Ε
Dtrace_0
Etrace_1
Ftrace_2
Gtrace_32Ϊ
$__inference_model_layer_call_fn_1194
$__inference_model_layer_call_fn_1437
$__inference_model_layer_call_fn_1454
$__inference_model_layer_call_fn_1313Ώ
Ά²²
FullArgSpec1
args)&
jself
jinputs

jtraining
jmask
varargs
 
varkw
 
defaults
p 

 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 zDtrace_0zEtrace_1zFtrace_2zGtrace_3
±
Htrace_0
Itrace_1
Jtrace_2
Ktrace_32Ζ
?__inference_model_layer_call_and_return_conditional_losses_1806
?__inference_model_layer_call_and_return_conditional_losses_2158
?__inference_model_layer_call_and_return_conditional_losses_1345
?__inference_model_layer_call_and_return_conditional_losses_1377Ώ
Ά²²
FullArgSpec1
args)&
jself
jinputs

jtraining
jmask
varargs
 
varkw
 
defaults
p 

 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 zHtrace_0zItrace_1zJtrace_2zKtrace_3
ΙBΖ
__inference__wrapped_model_775input_1"
²
FullArgSpec
args 
varargsjargs
varkwjkwargs
defaults
 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 
,
Lserving_default"
signature_map
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
­
Mnon_trainable_variables

Nlayers
Ometrics
Player_regularization_losses
Qlayer_metrics
	variables
trainable_variables
regularization_losses
__call__
*&call_and_return_all_conditional_losses
&"call_and_return_conditional_losses"
_generic_user_object
ο
Rtrace_02?
+__inference_q_activation_layer_call_fn_2163’
²
FullArgSpec
args
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 zRtrace_0

Strace_02ν
F__inference_q_activation_layer_call_and_return_conditional_losses_2194’
²
FullArgSpec
args
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 zStrace_0
"
_generic_user_object
.
 0
!1"
trackable_list_wrapper
.
 0
!1"
trackable_list_wrapper
'
=0"
trackable_list_wrapper
­
Tnon_trainable_variables

Ulayers
Vmetrics
Wlayer_regularization_losses
Xlayer_metrics
	variables
trainable_variables
regularization_losses
__call__
*&call_and_return_all_conditional_losses
&"call_and_return_conditional_losses"
_generic_user_object
κ
Ytrace_02Ν
&__inference_q_dense_layer_call_fn_2203’
²
FullArgSpec
args
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 zYtrace_0

Ztrace_02θ
A__inference_q_dense_layer_call_and_return_conditional_losses_2322’
²
FullArgSpec
args
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 zZtrace_0
"
_generic_user_object
,

[config"
trackable_dict_wrapper
"
_generic_user_object
.
0
1"
trackable_list_wrapper
"
_generic_user_object
 :9 2q_dense/kernel
: 2q_dense/bias
.
-0
.1"
trackable_list_wrapper
.
-0
.1"
trackable_list_wrapper
'
>0"
trackable_list_wrapper
­
\non_trainable_variables

]layers
^metrics
_layer_regularization_losses
`layer_metrics
"	variables
#trainable_variables
$regularization_losses
&__call__
*'&call_and_return_all_conditional_losses
&'"call_and_return_conditional_losses"
_generic_user_object
μ
atrace_02Ο
(__inference_q_dense_1_layer_call_fn_2331’
²
FullArgSpec
args
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 zatrace_0

btrace_02κ
C__inference_q_dense_1_layer_call_and_return_conditional_losses_2450’
²
FullArgSpec
args
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 zbtrace_0
"
_generic_user_object
,

cconfig"
trackable_dict_wrapper
"
_generic_user_object
.
(0
*1"
trackable_list_wrapper
"
_generic_user_object
":  2q_dense_1/kernel
:2q_dense_1/bias
.
;0
<1"
trackable_list_wrapper
.
;0
<1"
trackable_list_wrapper
 "
trackable_list_wrapper
­
dnon_trainable_variables

elayers
fmetrics
glayer_regularization_losses
hlayer_metrics
/	variables
0trainable_variables
1regularization_losses
3__call__
*4&call_and_return_all_conditional_losses
&4"call_and_return_conditional_losses"
_generic_user_object
ε
itrace_02Θ
!__inference_mu_layer_call_fn_2459’
²
FullArgSpec
args
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 zitrace_0

jtrace_02γ
<__inference_mu_layer_call_and_return_conditional_losses_2554’
²
FullArgSpec
args
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 zjtrace_0
,

kconfig"
trackable_dict_wrapper
,

lconfig"
trackable_dict_wrapper
"
_generic_user_object
"
_generic_user_object
.
70
81"
trackable_list_wrapper
"
_generic_user_object
:2	mu/kernel
:2mu/bias
Λ
mtrace_02?
__inference_loss_fn_0_2565
²
FullArgSpec
args 
varargs
 
varkw
 
defaults
 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *’ zmtrace_0
Λ
ntrace_02?
__inference_loss_fn_1_2576
²
FullArgSpec
args 
varargs
 
varkw
 
defaults
 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *’ zntrace_0
 "
trackable_list_wrapper
C
0
1
2
3
4"
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_dict_wrapper
φBσ
$__inference_model_layer_call_fn_1194input_1"Ώ
Ά²²
FullArgSpec1
args)&
jself
jinputs

jtraining
jmask
varargs
 
varkw
 
defaults
p 

 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 
υBς
$__inference_model_layer_call_fn_1437inputs"Ώ
Ά²²
FullArgSpec1
args)&
jself
jinputs

jtraining
jmask
varargs
 
varkw
 
defaults
p 

 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 
υBς
$__inference_model_layer_call_fn_1454inputs"Ώ
Ά²²
FullArgSpec1
args)&
jself
jinputs

jtraining
jmask
varargs
 
varkw
 
defaults
p 

 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 
φBσ
$__inference_model_layer_call_fn_1313input_1"Ώ
Ά²²
FullArgSpec1
args)&
jself
jinputs

jtraining
jmask
varargs
 
varkw
 
defaults
p 

 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 
B
?__inference_model_layer_call_and_return_conditional_losses_1806inputs"Ώ
Ά²²
FullArgSpec1
args)&
jself
jinputs

jtraining
jmask
varargs
 
varkw
 
defaults
p 

 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 
B
?__inference_model_layer_call_and_return_conditional_losses_2158inputs"Ώ
Ά²²
FullArgSpec1
args)&
jself
jinputs

jtraining
jmask
varargs
 
varkw
 
defaults
p 

 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 
B
?__inference_model_layer_call_and_return_conditional_losses_1345input_1"Ώ
Ά²²
FullArgSpec1
args)&
jself
jinputs

jtraining
jmask
varargs
 
varkw
 
defaults
p 

 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 
B
?__inference_model_layer_call_and_return_conditional_losses_1377input_1"Ώ
Ά²²
FullArgSpec1
args)&
jself
jinputs

jtraining
jmask
varargs
 
varkw
 
defaults
p 

 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 
ΙBΖ
"__inference_signature_wrapper_1408input_1"
²
FullArgSpec
args 
varargs
 
varkwjkwargs
defaults
 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_dict_wrapper
ίBά
+__inference_q_activation_layer_call_fn_2163inputs"’
²
FullArgSpec
args
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 
ϊBχ
F__inference_q_activation_layer_call_and_return_conditional_losses_2194inputs"’
²
FullArgSpec
args
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
'
=0"
trackable_list_wrapper
 "
trackable_dict_wrapper
ΪBΧ
&__inference_q_dense_layer_call_fn_2203inputs"’
²
FullArgSpec
args
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 
υBς
A__inference_q_dense_layer_call_and_return_conditional_losses_2322inputs"’
²
FullArgSpec
args
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 
 "
trackable_dict_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
'
>0"
trackable_list_wrapper
 "
trackable_dict_wrapper
άBΩ
(__inference_q_dense_1_layer_call_fn_2331inputs"’
²
FullArgSpec
args
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 
χBτ
C__inference_q_dense_1_layer_call_and_return_conditional_losses_2450inputs"’
²
FullArgSpec
args
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 
 "
trackable_dict_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_list_wrapper
 "
trackable_dict_wrapper
ΥB?
!__inference_mu_layer_call_fn_2459inputs"’
²
FullArgSpec
args
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 
πBν
<__inference_mu_layer_call_and_return_conditional_losses_2554inputs"’
²
FullArgSpec
args
jself
jinputs
varargs
 
varkw
 
defaults
 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *
 
 "
trackable_dict_wrapper
 "
trackable_dict_wrapper
±B?
__inference_loss_fn_0_2565"
²
FullArgSpec
args 
varargs
 
varkw
 
defaults
 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *’ 
±B?
__inference_loss_fn_1_2576"
²
FullArgSpec
args 
varargs
 
varkw
 
defaults
 

kwonlyargs 
kwonlydefaults
 
annotationsͺ *’ 
__inference__wrapped_model_775c !-.;<0’-
&’#
!
input_1?????????9
ͺ "'ͺ$
"
mu
mu?????????9
__inference_loss_fn_0_2565 ’

’ 
ͺ " 9
__inference_loss_fn_1_2576-’

’ 
ͺ " ¬
?__inference_model_layer_call_and_return_conditional_losses_1345i !-.;<8’5
.’+
!
input_1?????????9
p 

 
ͺ "%’"

0?????????
 ¬
?__inference_model_layer_call_and_return_conditional_losses_1377i !-.;<8’5
.’+
!
input_1?????????9
p

 
ͺ "%’"

0?????????
 «
?__inference_model_layer_call_and_return_conditional_losses_1806h !-.;<7’4
-’*
 
inputs?????????9
p 

 
ͺ "%’"

0?????????
 «
?__inference_model_layer_call_and_return_conditional_losses_2158h !-.;<7’4
-’*
 
inputs?????????9
p

 
ͺ "%’"

0?????????
 
$__inference_model_layer_call_fn_1194\ !-.;<8’5
.’+
!
input_1?????????9
p 

 
ͺ "?????????
$__inference_model_layer_call_fn_1313\ !-.;<8’5
.’+
!
input_1?????????9
p

 
ͺ "?????????
$__inference_model_layer_call_fn_1437[ !-.;<7’4
-’*
 
inputs?????????9
p 

 
ͺ "?????????
$__inference_model_layer_call_fn_1454[ !-.;<7’4
-’*
 
inputs?????????9
p

 
ͺ "?????????
<__inference_mu_layer_call_and_return_conditional_losses_2554\;</’,
%’"
 
inputs?????????
ͺ "%’"

0?????????
 t
!__inference_mu_layer_call_fn_2459O;</’,
%’"
 
inputs?????????
ͺ "?????????’
F__inference_q_activation_layer_call_and_return_conditional_losses_2194X/’,
%’"
 
inputs?????????9
ͺ "%’"

0?????????9
 z
+__inference_q_activation_layer_call_fn_2163K/’,
%’"
 
inputs?????????9
ͺ "?????????9£
C__inference_q_dense_1_layer_call_and_return_conditional_losses_2450\-./’,
%’"
 
inputs????????? 
ͺ "%’"

0?????????
 {
(__inference_q_dense_1_layer_call_fn_2331O-./’,
%’"
 
inputs????????? 
ͺ "?????????‘
A__inference_q_dense_layer_call_and_return_conditional_losses_2322\ !/’,
%’"
 
inputs?????????9
ͺ "%’"

0????????? 
 y
&__inference_q_dense_layer_call_fn_2203O !/’,
%’"
 
inputs?????????9
ͺ "????????? 
"__inference_signature_wrapper_1408n !-.;<;’8
’ 
1ͺ.
,
input_1!
input_1?????????9"'ͺ$
"
mu
mu?????????