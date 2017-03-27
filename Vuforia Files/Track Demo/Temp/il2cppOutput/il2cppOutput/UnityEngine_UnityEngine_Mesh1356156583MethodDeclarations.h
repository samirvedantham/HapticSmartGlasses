#pragma once

#include "il2cpp-config.h"

#ifndef _MSC_VER
# include <alloca.h>
#else
# include <malloc.h>
#endif

#include <stdint.h>
#include <assert.h>
#include <exception>

// UnityEngine.Mesh
struct Mesh_t1356156583;
// System.Array
struct Il2CppArray;
// System.Int32[]
struct Int32U5BU5D_t3030399641;
// UnityEngine.Vector3[]
struct Vector3U5BU5D_t1172311765;
// UnityEngine.Vector2[]
struct Vector2U5BU5D_t686124026;

#include "codegen/il2cpp-codegen.h"
#include "UnityEngine_UnityEngine_Mesh1356156583.h"
#include "UnityEngine_UnityEngine_Mesh_InternalShaderChannel3331827198.h"
#include "UnityEngine_UnityEngine_Mesh_InternalVertexChannel2178520045.h"
#include "mscorlib_System_Array3829468939.h"
#include "UnityEngine_UnityEngine_Bounds3033363703.h"

// System.Void UnityEngine.Mesh::.ctor()
extern "C"  void Mesh__ctor_m2975981674 (Mesh_t1356156583 * __this, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// System.Void UnityEngine.Mesh::Internal_Create(UnityEngine.Mesh)
extern "C"  void Mesh_Internal_Create_m1486058998 (Il2CppObject * __this /* static, unused */, Mesh_t1356156583 * ___mono0, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// System.Void UnityEngine.Mesh::Clear(System.Boolean)
extern "C"  void Mesh_Clear_m3100797454 (Mesh_t1356156583 * __this, bool ___keepVertexLayout0, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// System.Void UnityEngine.Mesh::Clear()
extern "C"  void Mesh_Clear_m231813403 (Mesh_t1356156583 * __this, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// System.Boolean UnityEngine.Mesh::get_canAccess()
extern "C"  bool Mesh_get_canAccess_m2763498171 (Mesh_t1356156583 * __this, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// System.Void UnityEngine.Mesh::PrintErrorCantAccessMesh(UnityEngine.Mesh/InternalShaderChannel)
extern "C"  void Mesh_PrintErrorCantAccessMesh_m2827771108 (Mesh_t1356156583 * __this, int32_t ___channel0, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// System.Void UnityEngine.Mesh::PrintErrorCantAccessMeshForIndices()
extern "C"  void Mesh_PrintErrorCantAccessMeshForIndices_m3276222682 (Mesh_t1356156583 * __this, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// System.Void UnityEngine.Mesh::SetArrayForChannelImpl(UnityEngine.Mesh/InternalShaderChannel,UnityEngine.Mesh/InternalVertexChannelType,System.Int32,System.Array,System.Int32)
extern "C"  void Mesh_SetArrayForChannelImpl_m271696022 (Mesh_t1356156583 * __this, int32_t ___channel0, int32_t ___format1, int32_t ___dim2, Il2CppArray * ___values3, int32_t ___arraySize4, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// System.Array UnityEngine.Mesh::GetAllocArrayFromChannelImpl(UnityEngine.Mesh/InternalShaderChannel,UnityEngine.Mesh/InternalVertexChannelType,System.Int32)
extern "C"  Il2CppArray * Mesh_GetAllocArrayFromChannelImpl_m1663415136 (Mesh_t1356156583 * __this, int32_t ___channel0, int32_t ___format1, int32_t ___dim2, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// System.Boolean UnityEngine.Mesh::HasChannel(UnityEngine.Mesh/InternalShaderChannel)
extern "C"  bool Mesh_HasChannel_m3616583481 (Mesh_t1356156583 * __this, int32_t ___channel0, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// System.Int32[] UnityEngine.Mesh::GetTrianglesImpl(System.Int32)
extern "C"  Int32U5BU5D_t3030399641* Mesh_GetTrianglesImpl_m3976840238 (Mesh_t1356156583 * __this, int32_t ___submesh0, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// System.Void UnityEngine.Mesh::SetTrianglesImpl(System.Int32,System.Array,System.Int32,System.Boolean)
extern "C"  void Mesh_SetTrianglesImpl_m2743099196 (Mesh_t1356156583 * __this, int32_t ___submesh0, Il2CppArray * ___triangles1, int32_t ___arraySize2, bool ___calculateBounds3, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// System.Void UnityEngine.Mesh::SetTrianglesImpl(System.Int32,System.Array,System.Int32)
extern "C"  void Mesh_SetTrianglesImpl_m540573335 (Mesh_t1356156583 * __this, int32_t ___submesh0, Il2CppArray * ___triangles1, int32_t ___arraySize2, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// UnityEngine.Bounds UnityEngine.Mesh::get_bounds()
extern "C"  Bounds_t3033363703  Mesh_get_bounds_m1752141467 (Mesh_t1356156583 * __this, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// System.Void UnityEngine.Mesh::INTERNAL_get_bounds(UnityEngine.Bounds&)
extern "C"  void Mesh_INTERNAL_get_bounds_m1331624142 (Mesh_t1356156583 * __this, Bounds_t3033363703 * ___value0, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// System.Void UnityEngine.Mesh::RecalculateNormals()
extern "C"  void Mesh_RecalculateNormals_m1034493793 (Mesh_t1356156583 * __this, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// System.Int32 UnityEngine.Mesh::get_vertexCount()
extern "C"  int32_t Mesh_get_vertexCount_m989566320 (Mesh_t1356156583 * __this, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// System.Int32 UnityEngine.Mesh::DefaultDimensionForChannel(UnityEngine.Mesh/InternalShaderChannel)
extern "C"  int32_t Mesh_DefaultDimensionForChannel_m153181993 (Il2CppObject * __this /* static, unused */, int32_t ___channel0, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// System.Int32 UnityEngine.Mesh::SafeLength(System.Array)
extern "C"  int32_t Mesh_SafeLength_m3028452891 (Mesh_t1356156583 * __this, Il2CppArray * ___values0, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// System.Void UnityEngine.Mesh::SetSizedArrayForChannel(UnityEngine.Mesh/InternalShaderChannel,UnityEngine.Mesh/InternalVertexChannelType,System.Int32,System.Array,System.Int32)
extern "C"  void Mesh_SetSizedArrayForChannel_m299035387 (Mesh_t1356156583 * __this, int32_t ___channel0, int32_t ___format1, int32_t ___dim2, Il2CppArray * ___values3, int32_t ___valuesCount4, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// UnityEngine.Vector3[] UnityEngine.Mesh::get_vertices()
extern "C"  Vector3U5BU5D_t1172311765* Mesh_get_vertices_m626989480 (Mesh_t1356156583 * __this, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// System.Void UnityEngine.Mesh::set_vertices(UnityEngine.Vector3[])
extern "C"  void Mesh_set_vertices_m2936804213 (Mesh_t1356156583 * __this, Vector3U5BU5D_t1172311765* ___value0, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// System.Void UnityEngine.Mesh::set_normals(UnityEngine.Vector3[])
extern "C"  void Mesh_set_normals_m2674236682 (Mesh_t1356156583 * __this, Vector3U5BU5D_t1172311765* ___value0, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// UnityEngine.Vector2[] UnityEngine.Mesh::get_uv()
extern "C"  Vector2U5BU5D_t686124026* Mesh_get_uv_m3811151337 (Mesh_t1356156583 * __this, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// System.Void UnityEngine.Mesh::set_uv(UnityEngine.Vector2[])
extern "C"  void Mesh_set_uv_m1497318906 (Mesh_t1356156583 * __this, Vector2U5BU5D_t686124026* ___value0, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// System.Int32[] UnityEngine.Mesh::get_triangles()
extern "C"  Int32U5BU5D_t3030399641* Mesh_get_triangles_m3988715512 (Mesh_t1356156583 * __this, const MethodInfo* method) IL2CPP_METHOD_ATTR;
// System.Void UnityEngine.Mesh::set_triangles(System.Int32[])
extern "C"  void Mesh_set_triangles_m3244966865 (Mesh_t1356156583 * __this, Int32U5BU5D_t3030399641* ___value0, const MethodInfo* method) IL2CPP_METHOD_ATTR;
